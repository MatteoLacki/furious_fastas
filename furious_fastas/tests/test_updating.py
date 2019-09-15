%load_ext autoreload
%autoreload 2

from pathlib import Path
from platform import system
from concurrent.futures import ThreadPoolExecutor

from furious_fastas.download import download
from furious_fastas.uniprot import uniprot_url

if system() == 'Darwin':
	path = Path('/Users/matteo/Projects/furious_fastas')
	db_path = path/'tests/threadpool/tests/threadpool/db0'
else:
	path = Path("/home/matteo/Projects/furious_fastas/gnl2sp4ute")


url2raw = set(uniprot_url.values())

%%time
res0 = {u:download(u) for u in url2raw}



%%time
with ThreadPoolExecutor() as e:
	res1 = dict(zip(url2raw, e.map(download, url2raw)))


