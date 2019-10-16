from furious_fastas.fasta import Fasta

f = Fasta('>test|test', 'PEPTIDEPEPTIDE')
g = Fasta('>test|test', 'EPTI')

g in f
f in g


list(f.where_is(g))
f.sequence[1:5]
f.sequence[8:12]
list(f.where_is('AZZZZ'))

from furious_fastas.seq_ops import covered_area

A = covered_area(sorted((s,e) for qc in qc_peps 
                                  for (s,e) in find_indices3(qc, qc_prot)))
    L = len(qc_prot)

sorted((s,e) for qc_pep in qc_peps for s,e in qc.where_is(qc_pep))


