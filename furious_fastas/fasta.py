class Fasta(object):
    """Class representing one particular fasta object."""
    def __init__(self, header, sequence):
        self.header = header
        self.sequence = sequence

    def __repr__(self):
        return "Fasta {}".format(self.header)

    def __str__(self):
        return self.sequence
