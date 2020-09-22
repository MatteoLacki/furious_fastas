%load_ext autoreload
%autoreload 2

from pathlib import Path
from platform import system
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint

from furious_fastas.download import download
from furious_fastas.uniprot import uniprot_url
from furious_fastas.update import update_plgs_peaks_fastas
from furious_fastas.parse import parse_settings
from furious_fastas.fastas import Fastas

url2raw = list(uniprot_url.values())
folder = Path("/home/matteo/Projects/furious_fastas")
uniprot = dict(parse_settings(folder/'data/uniprot.txt'))

url2raw = update_plgs_peaks_fastas(folder/'test_download', uniprot.items(), verbose=True)
for url, raw in url2raw.items():
    print(url)
    pprint(raw[:100])

human = Fastas()
human.parse(url2raw[uniprot['human'][0]])
yeast = Fastas()
yeast.parse(url2raw[uniprot['yeast'][0]])
hy = human + yeast

url2fs = {}
for url, raw in url2raw.items():
    fs = Fastas()
    fs.parse(raw)
    url2fs[url] = fs 

verbose = True
name, urls = 'hye', uniprot['hye']
for name, urls in uniprot.items():
    if verbose:
        print("\tUpdating {}.".format(name))
    FS = Fastas()
    for url in urls:
        FS += url2fs[url]
    file = "{}_{}_conts_{}_{}.fasta".format(name, str(len(fs)), str(len(contaminants)), NOW)
    FS.extend(contaminants)
    FS.write(latest_NOW_PEAKS/file)
    FS = Fastas(f.to_ncbi_general() for f in fs)
    FS.reverse()
    FS.write(latest_NOW_PLGS/file)