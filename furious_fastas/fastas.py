from Bio import SeqIO
import io
from itertools import chain
from os.path import join as pjoin
from os import path
import requests

from furious_fastas.uniprot import uniprot



class SimpleFastas(object):
    def read(self, path):
        """Read the fastas."""
        self.fastas = list(SeqIO.parse(path, "fasta"))

    def write(self, path, original = False):
        """Write file under the given path.

        Arguments
        =========
        path : str
            Path where to dump the file.
        """
        SeqIO.write(self.fastas, path, "fasta")

    def __iter__(self):
        """Iterate over sequences."""
        return iter(self.fastas)

    def __len__(self):
        """Return the number of sequences in the fasta file.""" 
        return len(self.fastas)



class Fastas(SimpleFastas):
    def __init__(self, uniprot_query = "http://www.uniprot.org/uniprot/?query="):
        """Initialize the class.

        Arguments
        =========
        uniprot_querry : str
            The url prepended to the query string.
            The default seems to be constant and it is in the interest of
            the Uniprot guys so that this remains so.
        """
        self.uniprot_query = uniprot_query

    def download_from_uniprot(self, what):
        """Download the query/species sequences from Uniprot.

        Arguments
        =========
        what : str
            Either a uniprot query, like "organism:643680&format=fasta",
            or one of predefined queries from the set of "human", "ecoli",
            "yeast", "mouse", "leishmania", or "wheat".
        """
        if what in uniprot:
            what = uniprot[what]
        self.original_file = requests.get(self.uniprot_query + what)
        self.fastas = list(SeqIO.parse(io.StringIO(self.original_file.text), "fasta"))

    def write_original_file(self, path):
        """Write the file orginally downloaded from the Uniprot."""
        with open(path, "w") as f:
            f.write(self.original_file.text)



class Contaminants(SimpleFastas):
    """A class representing the contaminants."""
    def __init__(self):
        here = path.abspath(path.dirname(__file__))
        self.read(pjoin(here, "data/contaminants.fasta")) 



def save_fastas(fastas, out_path):
    """Save fasta sequences into one, nicely parsable fasta file.

    Arguments
    =========
    fastas : list of furious_fastas.fastas.Fastas
        A list of fastas to merge.
    out_path : str
        A path where the merged fastas should be saved as one bigger fasta file.
    """
    all_sequences = chain.from_iterable(f for f in fastas)
    SeqIO.write(all_sequences, out_path, "fasta")
