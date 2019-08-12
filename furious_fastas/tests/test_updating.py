%load_ext autoreload
%autoreload 2


from furious_fastas import fastas, Fastas
from pathlib import Path
from furious_fastas.parse import parse_settings, parse_datestr


path = Path("/home/matteo/Projects/furious_fastas/gnl2sp4ute")
list(path.glob('*'))

human = fastas(path/"human.fasta")
hye = fastas(path/"HYE.fasta")
mouse = fastas(path/"mouse.fasta")

human.repeat_stats()
human.fasta_types()

settings_path = "/home/matteo/Projects/furious_fastas/test/species2uniprot.txt"
db_path = "/home/matteo/Projects/furious_fastas/test/new"
verbose = True
species2url = parse_settings(settings_path)

from pathlib import Path
from shutil import move as mv
from datetime import datetime

from furious_fastas.time_ops import datestr2date, now
from furious_fastas.fastas import fastas
from furious_fastas.contaminants import contaminants

# def update_folder(db_path, settings_path, verbose=True):
db_path = Path(db_path)
latest = db_path/'latest'
previous = db_path/'previous'
latest.mkdir(exist_ok=True, parents=True)
previous.mkdir(exist_ok=True, parents=True)

for f in latest.iterdir():
    if f.is_file():
        mv(src=str(latest/f), dst=str(previous))

now_str = now()

# name, url = next(species2url)
for name, url in species2url:
    fs = fastas(url)
    fs.extend(contaminants)
    file = "{}_{}_{}_{}.fasta".format(now_str, name, str(len(fastas)))
        fastas.write(current/file)
        if verbose:
            print("\t{} x".format(name))
    if verbose:
        print("Succeeeded!")

fs.fasta_types()
