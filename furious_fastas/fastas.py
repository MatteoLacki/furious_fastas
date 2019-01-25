import io
from itertools import chain
from os.path import join as pjoin
from os import path
import requests

from .uniprot import uniprot_url
from .parse.fastas import parse


class Fastas(object):
    def __init__(self):
        self.fastas = []
        self._reversed = False
        self._contaminated = False

    def read(self, path):
        """Read the fastas from file."""
        with open(path, 'r') as f:
            fastas = f.read()
        self.fastas = list(parse(fastas))

    def write(self, path, append=False):
        """Write file under the given path.

        Arguments
        =========
        path : str
            Path where to dump the file.
        """
        fp = 'a' if append else 'w+'
        with open(path, fp) as h:
            for f in self.fastas:
                h.write("{}\n{}\n".format(f.header, str(f)))

    def __iter__(self):
        """Iterate over sequences."""
        return iter(self.fastas)

    def __len__(self):
        """Return the number of sequences in the fasta file.""" 
        return len(self.fastas)

    def __getitem__(self, key):
        """Return the key-th fasta sequence."""
        return self.fastas[key]

    def __repr__(self):
        return "Fastas ({})".format(len(self))

    def reverse(self):
        """Add reversed sequences to the ones already present."""
        raise NotImplementedError
        if self._reversed == "not reversed":
            self._reversed = "reversed"



# class Contaminants(SimpleFastas):
#     """A class representing the contaminants.

#     This class cannot be downloaded from Uniprot.
#     But we give you some common contaminants for free.
#     """
#     def __init__(self):
#         here = path.abspath(path.dirname(__file__))
#         self.read(pjoin(here, "data/contaminants.fasta")) 
#         self.name = "contaminants"
#         self._reversed = "not reversed"

#     def __repr__(self):
#         return "Contaminants ({})".format(len(self))

# default_contaminants = Contaminants()



class Fastas(SimpleFastas):
    def download_from_uniprot(self, url):
        """Download the query/species sequences from Uniprot.

        Arguments
        =========
        url : str
            The url with uniprot query, e.g. 
            http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta
            is the one to retrieve all reviewed human proteins.
        """
        original_file = requests.get(uniprot_query).text
        self.fastas = list(parse(original_file))

    def add_contaminants(self, contaminants=default_contaminants):
        """Add contaminants to the fastas.

        Arguments
        =========
        contaminants : Fastas
            The input contaminants. By default, we use Tenzer's contaminants.
            I mean, the ones used in his groups, not biblically his.
        """
        if not self._contaminated:
            self.fastas.extend(contaminants)
            self._contaminated = True



class NamedFastas(Fastas):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def download_from_uniprot(self, uniprot_query=""):
        """Download the query/species sequences from Uniprot.

        Arguments
        =========
        uniprot_query : str
            The url to use to download the data from Uniprot.
            If not supplied, defaults to all reviewed human proteins found at
            http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta
        """
        self.uniprot_query = uniprot_query if uniprot_query else uniprot_url[self.name]
        self.original_file = requests.get(self.uniprot_query).text
        self.fastas = list(SeqIO.parse(io.StringIO(self.original_file), "fasta"))

    def __repr__(self):
        c = 'w/ contaminants' if self.contaminated else 'w/o contaminants'
        return "{} fastas, {}, {}.\n{}".format(self.name,
                                               c,
                                               self._reversed,
                                               self._seq_repr())


# human = NamedFastas("human")
# ecoli = NamedFastas("ecoli")
# wheat = NamedFastas("wheat")
# mouse = NamedFastas("mouse")
# yeast = NamedFastas("yeast")
# leishmania = NamedFastas("leishmania")



# def save(fastas, out_path):
#     """Save fasta sequences into one, nicely parsable fasta file.

#     Arguments
#     =========
#     fastas : list of furious_fastas.fastas.Fastas
#         A list of fastas to merge.
#     out_path : str
#         A path where the merged fastas should be saved as one bigger fasta file.
#     """
#     all_sequences = chain.from_iterable(f for f in fastas)
#     SeqIO.write(all_sequences, out_path, "fasta")
