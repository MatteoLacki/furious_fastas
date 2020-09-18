from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from shutil import move as mv
from datetime import datetime

from .contaminants import contaminants
from .download import download
from .fastas import Fastas
from .time_ops import datestr2date, now


def update_plgs_peaks_fastas(db_path, species2url, verbose=True):
    """Update fasta files.

    Args:
        db_path (str): Path to the folder where we will store the files.
        species2url (iterable of tuples): Each tuple consists of the species name and its Uniprot url.
        contaminants (Fastas): Fastas with contaminants.
        verbose (boolean): Be verbose.
    
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
    if verbose:
        print("Downloading files.")
    url2raw = {url for urls in species2url.values() for url in urls}

    with ThreadPoolExecutor() as e:
        ulr2raw = dict(zip(ulr2raw, e.map(download, url2raw)))
    # url2raw = {url:download(url) for url in url2raw}

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
    
    if verbose:
        print("Succeeeded!")
