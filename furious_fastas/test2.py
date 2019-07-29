from furious_fastas.download import download
from furious_fastas.uniprot import uniprot_url
from furious_fastas.parse import parse_uniprot_fastas
from furious_fastas.fastas import UniprotFastas

human_raw = download(uniprot_url['human'])

x = list(parse_uniprot_fastas(human_raw))
ten_prots = x[0:10]

unif = UniprotFastas()
unif.fastas = ten_prots

unif.write('/home/matteo/Projects/furious_fastas/data/tests/human10.fasta')
