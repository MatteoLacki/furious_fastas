%load_ext autoreload
%autoreload 2

import requests

from furious_fastas.fastas import Fastas
from furious_fastas.parse.fastas import parse

query = "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta"

fastas = requests.get(query).text
parsed_fastas = list(parse(fastas))

nf = NamedFastas('human')
fp = "/Users/matteo/Projects/furious_fastas/fastas/20180913_up_human_reviewed_20394entries.fasta"

nf.read(fp)
