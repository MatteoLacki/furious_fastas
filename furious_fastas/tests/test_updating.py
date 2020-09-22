%load_ext autoreload
%autoreload 2

from pathlib import Path
from platform import system
from concurrent.futures import ThreadPoolExecutor

from furious_fastas.download import download
from furious_fastas.uniprot import uniprot_url
from furious_fastas.update import update_plgs_peaks_fastas
from furious_fastas.parse import parse_settings

url2raw = list(uniprot_url.values())

%%time
res0 = {u:download(u) for u in url2raw[:3]}
# CPU times: user 2.42 s, sys: 677 ms, total: 3.1 s
# Wall time: 3min 46s

res2 = {}
for u in url2raw:
    res2[u] = download(u)


%%time
with ThreadPoolExecutor() as e:
	res1 = dict(zip(url2raw, e.map(download, url2raw)))
# CPU times: user 2.43 s, sys: 614 ms, total: 3.04 s
# Wall time: 47.1 s
folder = Path("/home/matteo/Projects/furious_fastas")
parse_settings(folder/'data/uniprot.txt')

species2url = [('human', (uniprot_url['human'],)),]
update_plgs_peaks_fastas(folder/'tests', species2url)

# TODO: the bloody thing has reversed sequences upon update.