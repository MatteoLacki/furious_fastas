%load_ext autoreload
%autoreload 2

# path2human = "/home/matteo/Projects/furious_fastas/4peaks/human.fasta"
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

from furious_fastas.update.peaks import update_peaks
from furious_fastas.update.plgs import update_plgs
from furious_fastas.contaminants import conts
from furious_fastas.download import download
from furious_fastas.fasta import Fasta, UniprotFasta, NCBIgeneralFasta
from furious_fastas.fastas import Fastas, UniprotFastas


from collections import Counter

# s2u = list(parse("/home/matteo/Projects/furious_fastas/4peaks/s2u2"))
# update_plgs("/home/matteo/Projects/furious_fastas/4peaks/db2", s2u)
# db_path = "/home/matteo/Projects/furious_fastas/4peaks/db2"
# species2url = s2u



human = UniprotFastas(human_raw)



with open("/home/matteo/Projects/furious_fastas/data/human_raw.fasta", 'w') as f:
	for r in human_raw:
		f.write(r)

import re

header = ">sp|P14060|3BHS1_HUMAN 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase"
header = ">sp|P14060|3BHS1_HUMAN 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase type 1 OS=Homo sapiens OX=9606 GN=HSD3B1 PE=1 SV=2"

%load_ext autoreload
%autoreload 2

from furious_fastas.contaminants import uniprot_contaminants
from furious_fastas.fastas import UniprotFastas, NCBIgeneralFastas
from furious_fastas.download import download
from furious_fastas.parse.fastas import parse_uniprot_fastas

uf == uf
uf == uniprot_contaminants


uf = UniprotFastas()
uf.append(uniprot_contaminants)
uf.append(uf)
uf + uf

uniprot_contaminants + uniprot_contaminants
uniprot_contaminants.append(uniprot_contaminants)

human = UniprotFastas()
human_raw = download("http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta")
human.parse_raw(human_raw)


human_uni = UniprotFastas()
human_uni.read('/home/matteo/Projects/furious_fastas/data/human_raw.fasta')
human_uni.append(uniprot_contaminants)
human_gnl = human_uni.to_ncbi_general()

human_gnl.write('/home/matteo/Projects/furious_fastas/data/human_raw_gnl.fasta')
human_gnl = NCBIgeneralFastas()
human_gnl.read('/home/matteo/Projects/furious_fastas/data/human_raw_gnl.fasta')
