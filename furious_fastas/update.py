from concurrent.futures import ThreadPoolExecutor
import logging
from pathlib import Path
from shutil import move as mv
from pprint import pprint
import gzip

from .contaminants import contaminants
from .download import download
from .fastas import Fastas
from .time_ops import datestr2date, now


logger = logging.getLogger(__name__)


def update_plgs_peaks_fastas(db_path,
                             species2urls,
                             verbose=False):
    """Update fasta files.

    An example of an input:
    ('hye', (''))

    Args:
        db_path (str): Path to the folder where we will store the files.
        species2urls (dict,iterable of tuples): Each tuple consists of the species name and its (potentially several) Uniprot url.
        verbose (boolean): increase verbosity.
    Returns:
        contaminants (Fastas): Fastas with contaminants.
    """
    if db_path == '.':
        db_path = Path.cwd()
    db_path = Path(db_path).expanduser()
    latest = db_path/'latest'
    previous = db_path/'previous'
    if latest.exists():
        previous.mkdir(exist_ok=True, parents=True)
        for f in latest.iterdir():
            mv(src=str(latest/f), dst=str(previous))
    NOW = now()
    latest_NOW = latest/NOW
    species2urls = dict(species2urls)

    logger.info("Downloading files.")
    urls = {url for urls in species2urls.values() for url in urls}
    if verbose:
        print('Going to download:')
        pprint(urls)
    with ThreadPoolExecutor() as e:
        raw_fastas = list(e.map(download, urls)) 
    if verbose: print("Downloaded. Parsing fastas.")

    url2fs = {}
    for url, raw in zip(urls, raw_fastas):
        fs = Fastas()
        fs.parse(raw)
        url2fs[url] = fs 

    if verbose: print("Parsed. Updating files.")
    for name, urls in species2urls.items():
        if verbose: print("\tUpdating {}.".format(name))
        fs = Fastas()
        for url in urls:
            fs += url2fs[url]
        stem = f"{name}_{len(fs)}_{NOW}"
        fs.write(latest_NOW/(stem+".fasta"))
        FS = fs.to_ncbi_general()
        FS.write(latest_NOW/(stem+"_pipelineFriendly.fasta"))
        fs.extend(contaminants)
        stem += f"_contaminants_{len(contaminants)}"
        fs.write(latest_NOW/(stem+".fasta"))
        FS.extend(contaminants.to_ncbi_general())
        FS.write(latest_NOW/(stem+"_pipelineFriendly.fasta"))        
        fs.reverse()
        stem += f"_reversed"
        fs.write(latest_NOW/(stem+".fasta"))
        FS.reverse()
        FS.write(latest_NOW/(stem+"_pipelineFriendly.fasta"))
    logger.info("Succeeeded!")

