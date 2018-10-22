import requests


uniprot = {}

humanUrl="http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta"
yeastUrl="http://www.uniprot.org/uniprot/?query=organism:643680&format=fasta"
ecoliUrl="http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:83333&format=fasta"


code = "Q7Z7W5"
data = urllib.request.urlopen("http://www.uniprot.org/uniprot/" + code + ".txt").read()


res = requests.get(yeastUrl)
res.text