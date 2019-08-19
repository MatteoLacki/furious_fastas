from pathlib import Path
from shutil import move as mv
from datetime import datetime

from furious_fastas.time_ops import datestr2date, now
from furious_fastas.fastas import fastas, Fastas
from furious_fastas.contaminants import contaminants


def update_plgs_peaks_fastas(db_path, species2url, verbose=True):
    """Update fasta files.

    Args:
        db_path (str): Path to the folder where we will store the files.
        species2url (iterable of tuples): Each tuple consists of the species name and its Uniprot url.
        contaminants (Fastas): Fastas with contaminants.
        verbose (boolean): Be verbose.
    
    """
    db_path = Path(db_path)
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

    for name, url in species2url:
        if verbose:
            print("\tUpdating {}.".format(name))
        fs = fastas(url)
        fs.extend(contaminants)
        file = "{}_{}_{}.fasta".format(name, str(len(fs)), NOW)
        fs.write(latest_NOW_PEAKS/file)
        fs = Fastas(f.to_ncbi_general() for f in fs)
        fs.reverse()
        fs.write(latest_NOW_PLGS/file)
    if verbose:
        print("Succeeeded!")
