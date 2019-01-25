%load_ext autoreload
%autoreload 2

from furious_fastas.fastas import NamedFastas

nf = NamedFastas('human')
fp = "/Users/matteo/Projects/furious_fastas/fastas/20180913_up_human_reviewed_20394entries.fasta"

nf.read(fp)
