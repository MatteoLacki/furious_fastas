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
# CPU times: user 2.42 s, sys: 677 ms, total: 3.1 s
# Wall time: 3min 46s

%%time
with ThreadPoolExecutor() as e:
	res1 = dict(zip(url2raw, e.map(download, url2raw)))
# CPU times: user 2.43 s, sys: 614 ms, total: 3.04 s
# Wall time: 47.1 s

