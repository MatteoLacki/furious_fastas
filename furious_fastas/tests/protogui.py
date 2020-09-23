%load_ext autoreload
%autoreload 2

from pathlib import Path

from furious_fastas.protogui import fasta_path_gui


p = Path('/home/matteo/Projects/furious_fastas/test_download/latest')
db = list(p.glob('*'))[0]

fastas_gui(db)


