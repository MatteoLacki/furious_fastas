uniprot_query = "http://www.uniprot.org/uniprot/?query="

uniprot = {
    "human": uniprot_query + "reviewed:yes+AND+organism:9606&format=fasta",
    "yeast": uniprot_query + "organism:643680&format=fasta",
    "ecoli": uniprot_query + "reviewed:yes+AND+organism:83333&format=fasta",
    "wheat": uniprot_query + "organism:4565&format=fasta",
    "mouse": uniprot_query + "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:10090&format=fasta",
    "leishmania" : uniprot_query + "http://www.uniprot.org/uniprot/?query=organism:5664&format=fasta"
}