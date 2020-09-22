from .seq_ops import covered_area


class Fasta(object):
    """Class representing one particular fasta object."""
    def __init__(self, header, sequence):
        self.sequence = sequence
        self.header = header

    def __repr__(self):
        # return "{}({})".format(self.__class__.__name__, self.header)
        return self.header

    def __str__(self):
        return self.sequence

    def reverse(self):
        """Reverse a fasta, customizing the header."""
        return self.__class__(self.header+" REVERSED", self.sequence[::-1])

    def copy(self):
        """Copy a fasta object."""
        return self.__class__(self.header, self.sequence)

    def __hash__(self):
        return hash((self.sequence, self.header))

    def __eq__(self, other):
        return self.header == other.header and self.sequence == other.sequence

    def __len__(self):
        return len(self.sequence)

    def __contains__(self, other):
        """Check if the other protein is a subsequence.

        Args:
            other (str,Fasta): the other Fasta or a sequence.
        Returns:
            boolean: Is a sequence?"""
        return str(other) in self.sequence

    def where_is(self, other):
        """Find pairs of indices that the other Fasta's sequence occupies in the sequence.

        Used to establish positions of subsequences.

        Args:
            other (str,Fasta): the other Fasta or a sequence.
        """
        s = str(other) # subsequence
        n = len(s)
        if n > 0:
            i = 0
            for h in self.sequence.split(s)[0:-1]:
                i += len(h)
                yield i,i+n
                i += n

    def coverage(self, others):
        """Calculate the coverage of the current fasta with other fastas or sequences.

        Args:
            others (iterable of str of Fasta, or Fastas): What should be covering the current fasta?
        Returns:
            float: Coverage (between 0 and 1) of that sequence by others.
        """
        A = covered_area(sorted((s,e) for other in others for s,e in self.where_is(other)))
        L = len(self.sequence)
        return A/L


class ParsedFasta(Fasta):
    def __init__(self, accession, entry, description, sequence):
        self.accession = accession
        self.entry = entry
        self.description = description
        self.sequence = sequence

    def to_swissprot(self):
        """Copy a fasta in Swiss Prot format."""
        return SwissProtFasta(self.accession, self.entry, self.description, self.sequence)

    def to_trembl(self):
        """Copy a fasta in TRembl format."""
        return TRemblFasta(self.accession, self.entry, self.description, self.sequence)

    def to_ncbi_general(self):
        """Copy a fasta in NCBI general format."""
        return NCBIgeneralFasta(self.accession, self.entry, self.description, self.sequence)

    def __repr__(self):
        return "{}({}|{}|{})".format(self.__class__.__name__, self.accession, self.entry, self.description)

    @property
    def header(self):
        raise NotImplementedError("Header must be a valid fiel/accessor of any subclass of the ParsedFasta.")


class SwissProtFasta(ParsedFasta):
    def reverse(self, i=''):
        """Reverse a fasta, customizing the header."""
        return Fasta('>REVERSE{} Reversed Sequence {}'.format(str(i), str(i)), self.sequence[::-1])

    @property
    def header(self):
        return ">sp|{}|{} {}".format(self.accession, self.entry, self.description)


class TRemblFasta(ParsedFasta):
    def reverse(self, i=''):
        """Reverse a fasta, customizing the header."""
        return Fasta('>REVERSE{} Reversed Sequence {}'.format(str(i), str(i)), self.sequence[::-1])

    @property
    def header(self):
        return ">tr|{}|{} {}".format(self.accession, self.entry, self.description)


class NCBIgeneralFasta(ParsedFasta):
    def reverse(self, i=''):
        return Fasta('>gnl|db|REVERSE{} REVERSE{} Reversed Sequence {}'.format(str(i), str(i), str(i)), self.sequence[::-1])        
    @property
    def header(self):
        return ">gnl|db|{} {} {}".format(self.accession, self.entry, self.description)


def parse_header(h):
    """Parse a fasta header.

    Args:
        h (str): the header.
    Returns:
        tuple: accession, entry, description and database tag.
     """
    if ">gnl|db|" in h:
        h = h.replace(">gnl|db|","")
        accession, entry = h.split(' ')[:2]
        description = h.replace(accession +' '+ entry + ' ', '')
        db = ">gnl|db|"
    elif '>sp|' in h:
        h = h.replace('>sp|','')
        accession, h = h.split('|')
        entry = h.split(' ')[0]
        description = h.replace(entry+' ','')
        db = ">sp|"
    elif '>tr|' in h:
        h = h.replace('>tr|','')
        accession, h = h.split('|')
        entry = h.split(' ')[0]
        description = h.replace(entry+' ','')
        db = ">tr|"
    elif ">REVERSE" in h:
        h = h.replace('>','')
        accession = entry = h.split(' ')[0]
        description = h.replace(entry+' ','')
        db = ">sp|"
    else:
        raise RuntimeError("Header cannot be parsed: {}".format(h))
    return accession, entry, description, db


fasta_formats = {'>sp|':      SwissProtFasta,
                 '>tr|':      TRemblFasta,
                 '>gnl|db|':  NCBIgeneralFasta}


def fasta(header, sequence):
    """Create a fasta object from header and sequence."""
    try:
        accession, entry, description, db = parse_header(header)
        fasta_format = fasta_formats.get(db, Fasta)
        return fasta_format(accession, entry, description, sequence)
    except RuntimeError:
        return Fasta(header, sequence)
