%load_ext autoreload
%autoreload 2

# path2human = "/home/matteo/Projects/furious_fastas/4peaks/human.fasta"
# path2human = "/Users/matteo/Projects/furious_fastas/test/human.fasta"

from furious_fastas.parse import parse_uniprot_fastas
from furious_fastas import UniprotFastas, NCBIgeneralFastas

from pathlib import Path

pp = Path("/Users/matteo/Projects/furious_fastas/")

human = UniprotFastas()
human.read(pp/"data/human_raw.fasta")

# check for the same sequences
from collections import Counter, defaultdict

rep_seq_prots = defaultdict(list)
prot_seqs = {}
for f in human:
	seq = str(f)
	if seq in prot_seqs:
		if not seq in rep_seq_prots:# need to add previous f
			rep_seq_prots[seq].append(prot_seqs[seq])
		rep_seq_prots[seq].append(f)
	else:
		prot_seqs[seq] = f

# there are 48 repetitions!!!
len(rep_seq_prots)

# how to deal with these???
from pprint import pprint

print(rep_seq_prots,
      file=open(pp/"tests/multiple_proteins_same_sequence.txt", "a"))






contaminants = UniprotFastas()
contaminants.read(pp/"data/contaminants.fasta")
str(contaminants[171])

human.append(contaminants)
human_gnl = human.to_ncbi_general()
human_gnl.add_reversed_fastas_for_plgs()
human_gnl.write(pp/'data/human_gnl_reversed.fas')

from furious_fastas.parse_conf_file import parse_conf

# species to url
s2u = list(parse_conf(pp/"tests/test_conf.txt"))

from furious_fastas.update.peaks import update_peaks_fasta_db
from furious_fastas.update.plgs import update_plgs_fasta_db


conts = [('contaminants', 'https://raw.githubusercontent.com/MatteoLacki/protein_contaminants/master/contaminants.fasta')]
db_path = pp/"tests/peaks/db"
update_peaks_fasta_db(db_path, conts)




update_plgs("/home/matteo/Projects/furious_fastas/4peaks/db2", s2u)
db_path = "/home/matteo/Projects/furious_fastas/4peaks/db2"
species2url = s2u



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
human_gnl.add_reversed_fastas_for_plgs()
human_gnl.write('/home/matteo/Projects/furious_fastas/data/human_gnl_reversed.fasta')