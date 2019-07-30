%load_ext autoreload
%autoreload 2

from furious_fastas.fastas import Fastas
from furious_fastas.fasta import Fasta
from collections import Counter
from furious_fastas.contaminants import contaminants

# human_raw = download(uniprot_url['human'])
human = Fastas()
path = r'/Users/matteo/Projects/furious_fastas/data/human_raw.fasta'
human.read(path)
human.repeat_stats()

human.write(r'/Users/matteo/Projects/furious_fastas/data/matteo_test.fasta')
human[0]
human[10]

contaminated_human = human + contaminants
contaminated_human.repeat_stats()
contaminants.repeat_stats()


human[0]