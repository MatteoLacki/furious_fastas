from furious_fastas import fastas, Fastas
from pathlib import Path

path = Path("/home/matteo/Projects/furious_fastas/gnl2sp4ute")
list(path.glob('*'))

human = fastas(path/"human.fasta")
hye = fastas(path/"HYE.fasta")
mouse = fastas(path/"mouse.fasta")

def filter_reverses_and_uniprotofy(F):
    return Fastas(f.to_swissprot() for f in F if not "REVERSE" in f.header)

human = filter_reverses_and_uniprotofy(human)
hye = filter_reverses_and_uniprotofy(hye)
mouse = filter_reverses_and_uniprotofy(mouse)

human.write(path/"human_sp.fasta")
hye.write(path/"hye_sp.fasta")
mouse.write(path/"mouse_sp.fasta")