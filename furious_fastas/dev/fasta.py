from furious_fastas.fasta import Fasta

f = Fasta('>test|test', 'PEPTIDEPEPTIDE')
g = Fasta('>test|test', 'EPTI')

g in f
f in g


list(f.where_is(g))
f.sequence[1:5]
f.sequence[8:12]
list(f.where_is('AZZZZ'))