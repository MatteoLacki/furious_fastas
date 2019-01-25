%load_ext autoreload
%autoreload 2

## works!!!
# from furious_fastas.download import download
# url = "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta"
# human = download(url)
# human.write("/Users/matteo/Projects/furious_fastas/test/human.fasta")

# # works!!!
# from furious_fastas.fastas import Fastas
# from furious_fastas.contaminants import conts
# human = Fastas()
# human.read("/Users/matteo/Projects/furious_fastas/test/human.fasta")
# human + conts

# # works!!!
# from furious_fastas.fasta import Fasta
# w = Fasta('h', 'AAADA')
# z = w.copy()
# w.h = 'wqe'

# # works!
# from furious_fastas.contaminants import get_tenzer_contaminants
# conts = get_tenzer_contaminants()

