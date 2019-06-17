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
from furious_fastas.update.plgs import update_plgs

s2u = list(parse("/home/matteo/Projects/furious_fastas/4peaks/s2u2"))
update_plgs("/home/matteo/Projects/furious_fastas/4peaks/db2", s2u)


db_path = "/home/matteo/Projects/furious_fastas/4peaks/db2"
species2url = s2u

from furious_fastas.contaminants import conts
from furious_fastas.download import download
from furious_fastas.fasta import Fasta
from furious_fastas.download import download

prot = human[0]
f = Fasta(prot.header, prot.sequence)
f.format
f.reformat()

uniprot = prot.header
db, prot, desc = uniprot.split('|')
a = ">gnl|db|{} {}".format(prot, desc)
b =">gnl|db|P46777 RL5_HUMAN 60S ribosomal protein L5 OS=Homo sapiens OX=9606 GN=RPL5 PE=1 SV=3"

fasta_format, db, rest = a.split('|')
a == b


for f in human:
	try:
		db, prot, desc = f.header.split('|')
	except ValueError:
		print(f.header)

human[0].header

db, prot, desc = uniprot.split('|')


human_raw = download("http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta", True)
strange_fasta = '>4-isomerase type 1 OS=Homo sapiens OX=9606 GN=HSD3B1 PE=1 SV=2'



with open("/home/matteo/Projects/furious_fastas/data/human_raw.fasta", 'w') as f:
	for r in human_raw:
		f.write(r)

import re

header = ">sp|P14060|3BHS1_HUMAN 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase"
header = ">sp|P14060|3BHS1_HUMAN 3 beta-hydroxysteroid dehydrogenase/Delta 5-->4-isomerase type 1 OS=Homo sapiens OX=9606 GN=HSD3B1 PE=1 SV=2"



m = re.finditer(header_pattern, human_raw)
w = next(m)
w[1]
w[2]
w[3] 