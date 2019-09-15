
%load_ext autoreload
%autoreload 2

from furious_fastas import fastas, Fastas
from furious_fastas.fastas import iter_chunks

path = Path("/home/matteo/Projects/furious_fastas/gnl2sp4ute")
human = fastas(path/"human.fasta")

for h in human:
    if h.header == ">gnl|db|P58511 SI11A_HUMAN Small integral membrane protein 11A OS=Homo sapiens OX=9606 GN=SMIM11A PE=2 SV=1":
        w = h
w
len(w)
list(iter_chunks(w.sequence, 10))


human.write("/home/matteo/Projects/furious_fastas/test/so_human.fasta")
so_human = fastas("/home/matteo/Projects/furious_fastas/test/so_human.fasta")

all(a == b for a,b in zip(human, so_human))