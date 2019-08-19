%load_ext autoreload
%autoreload 2

from furious_fastas.parse import parse_settings

p0 = "/home/matteo/Projects/furious_fastas/test/species2uniprot.txt"
list(parse_settings(p0))

p1 = "/home/matteo/Projects/furious_fastas/test/hye.txt"
x = dict(parse_settings(p1))

p2 = "/home/matteo/Projects/furious_fastas/test/ecoli_leishmania_mix.txt"
x = dict(parse_settings(p2))



from furious_fastas.download import download

url2raw = {url for urls in x.values() for url in urls}
url2raw = {url:download(url) for url in url2raw}
