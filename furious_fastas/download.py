import requests

from .parse.fastas import parse
from .fastas import Fastas


def download(url, raw=False):
    """Download the query/species sequences from Uniprot.

    Arguments
    =========
    url : str
        The url with uniprot query, e.g. 
        http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta
        is the one to retrieve all reviewed human proteins.
    """
    fastas = requests.get(url).text
    if raw:
        return fastas
    else:
        return Fastas(list(parse(fastas)))
