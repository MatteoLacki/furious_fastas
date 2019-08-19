%load_ext autoreload
%autoreload 2

from pathlib import Path

from furious_fastas import fastas
from furious_fastas.parse import parse_settings
from furious_fastas.update import update_plgs_peaks_fastas


path = Path("/home/matteo/Projects/furious_fastas/gnl2sp4ute")
human = fastas(path/"human.fasta")
hye = fastas(path/"HYE.fasta")
mouse = fastas(path/"mouse.fasta")

settings_path = "/home/matteo/Projects/furious_fastas/test/species2uniprot.txt"
db_path = "/home/matteo/Projects/furious_fastas/test/new"
verbose = True
species2url = list(parse_settings(settings_path))
db_path = "/home/matteo/Projects/furious_fastas/test/new"

small = [
    ('ecoli',"http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:83333&format=fasta"),
    ('leishmania',"http://www.uniprot.org/uniprot/?query=organism:5664&format=fasta")]

update_plgs_peaks_fastas(db_path, small)
update_plgs_peaks_fastas(db_path, species2url)


Path('.').expanduser()
Path.cwd()

p = "/home/matteo/Projects/furious_fastas/test/new/latest/2019-8-19_13-57-22/PLGS/ecoli_4691_2019-8-19_13-57-22.fasta"


