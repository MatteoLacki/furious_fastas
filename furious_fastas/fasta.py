import re

uniprot_pattern = re.compile(r">(.+)\|(.+)\|(.*)")
gnl_pattern = re.compile()

class Fasta(object):
    """Class representing one particular fasta object."""
    def __init__(self, sequence, header):
        self.sequence = sequence
        self.header = header

    def __repr__(self):
        return "Fasta({})".format(self.header)

    def __str__(self):
        return self.sequence

    def reverse(self):
        #TODO: modify the header
        new_header = self.header
        return Fasta(new_header, self.sequence[::-1])

    def copy(self):
        return Fasta(self.header, self.sequence)


class UniprotFasta(Fasta):
    """Fasta with a uniprot header."""
    def __init__(self, sequence, header=''):
        if not header:
            header, sequence = re.match(header_pattern, header)
        super().__init__(sequence, header)

    def to_gnl(self):
        """Reformat the uniprot header to general ncbi format."""
        db, prot, desc = self.header.split('|')
        new_header = ">gnl|db|{} {}".format(prot, desc)
        return NCBIgeneralFasta(new_header, self.sequence)

    def to_ncbi_general(self):
        """Reformat the uniprot header to general ncbi format."""
        return self.to_gnl()


class NCBIgeneralFasta(Fasta):
    """Fasta with a ncbi general header (according to PLGS)."""

    def to_uniprot(self):
        """Reformat the NCBI general header to uniprot format."""
        