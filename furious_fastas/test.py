%load_ext autoreload
%autoreload 2

path2human = "/home/matteo/Projects/furious_fastas/4peaks/human.fasta"
# path2human = "/Users/matteo/Projects/furious_fastas/test/human.fasta"

## works!!!
# from furious_fastas.download import download
# url = "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta"
# human = download(url)
# human.write(path2human)

# # works!!!
# from furious_fastas.fastas import Fastas
# from furious_fastas.contaminants import conts
# human = Fastas()
# human.read(path2human)
# human
# human + conts

from furious_fastas.parse.species2uniprot import parse
from furious_fastas.update.peaks import update_peaks

s2u = list(parse("/home/matteo/Projects/furious_fastas/4peaks/s2u0"))
update_peaks("/home/matteo/Projects/furious_fastas/4peaks/db", s2u)