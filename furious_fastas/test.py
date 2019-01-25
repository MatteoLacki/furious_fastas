%load_ext autoreload
%autoreload 2

from furious_fastas.download import download

url = "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta"

human = download(url)
human.write("/Users/matteo/Projects/furious_fastas/test/human.fasta")


from furious_fastas.fastas import Fastas
from furious_fastas.parse.fastas import parse


fastas = requests.get(query).text
parsed_fastas = list(parse(fastas))

nf = NamedFastas('human')
fp = "/Users/matteo/Projects/furious_fastas/fastas/20180913_up_human_reviewed_20394entries.fasta"

nf.read(fp)


# # works!
# from furious_fastas.contaminants import get_tenzer_contaminants
# conts = get_tenzer_contaminants()

