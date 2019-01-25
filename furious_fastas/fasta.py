class Fasta(object):
    """Class representing one particular fasta object."""
    def __init__(self, header, sequence):
        self.h = header
        self.s = sequence

    def __repr__(self):
        return "Fasta {}".format(self.h)

    def __str__(self):
        return self.s
