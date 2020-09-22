from concurrent.futures import ThreadPoolExecutor
import logging
from pathlib import Path
from shutil import move as mv

from .contaminants import contaminants
from .download import download
from .fastas import Fastas
from .time_ops import datestr2date, now


logger = logging.getLogger(__name__)


def update_plgs_peaks_fastas(db_path,
                             species2url,
                             verbose=False):
    """Update fasta files.

    An example of an input:
    ('hye', (''))

    Args:
        db_path (str): Path to the folder where we will store the files.
        species2url (iterable of tuples): Each tuple consists of the species name and its (potentially several) Uniprot url.
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
    latest_NOW_PEAKS = latest/NOW/'PEAKS'
    latest_NOW_PLGS = latest/NOW/'PLGS'
    latest_NOW_PEAKS.mkdir(exist_ok=True, parents=True)
    latest_NOW_PLGS.mkdir(exist_ok=True, parents=True)

    # avoid multiple downloads of the same files
    species2url = dict(species2url)
    logger.info("Downloading files.")

    url2raw = {url for urls in species2url.values() for url in urls}
    with ThreadPoolExecutor() as e:
        url2raw = dict(zip(url2raw, e.map(download, url2raw)))
    
    for name, urls in species2url.items():
        if verbose:
            print("\tUpdating {}.".format(name))
        fs = Fastas()
        for url in urls:
            fs.parse(url2raw[url])
        file = "{}_{}_conts_{}_{}.fasta".format(name, str(len(fs)), str(len(contaminants)), NOW)
        fs.extend(contaminants)
        fs.write(latest_NOW_PEAKS/file)
        fs = Fastas(f.to_ncbi_general() for f in fs)
        fs.reverse()
        fs.write(latest_NOW_PLGS/file)
    
    logger.info("Succeeeded!")

