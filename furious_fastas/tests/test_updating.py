%load_ext autoreload
%autoreload 2

from furious_fastas import fastas, Fastas
from pathlib import Path
from furious_fastas.parse import parse_settings
from furious_fastas.time_ops import datestr2date
from furious_fastas.update import update_plgs_peaks_fastas


path = Path("/home/matteo/Projects/furious_fastas/gnl2sp4ute")
human = fastas(path/"human.fasta")
hye = fastas(path/"HYE.fasta")
mouse = fastas(path/"mouse.fasta")

human.repeat_stats()
human.fasta_types()

settings_path = "/home/matteo/Projects/furious_fastas/test/species2uniprot.txt"
db_path = "/home/matteo/Projects/furious_fastas/test/new"
verbose = True
species2url = parse_settings(settings_path)

db_path = "/home/matteo/Projects/furious_fastas/test/new"
small = [
    ('ecoli',"http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:83333&format=fasta"),
    ('leishmania',"http://www.uniprot.org/uniprot/?query=organism:5664&format=fasta")]

update_plgs_peaks_fastas(db_path, small)


f = human[0]

f.sequence

line_length = 80
len(f.sequence) // line_length


x = f.sequence
chunk_size=80


list(divide_into_chunks(f.sequence, 10))
len(f.sequence)


human.write("/home/matteo/Projects/furious_fastas/test/so_human.fasta")