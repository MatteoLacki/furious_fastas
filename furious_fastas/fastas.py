"""Classes representing collections of fastas."""
from collections import Counter
from pathlib import Path

from .fasta import fasta
from .download import download


def iter_chunks(x, chunk_size=80):
    """Iterate over chunks of a given size.

    The last chunk can be smaller than others.

    Args:
        x (str or list): or something that supports get operation.
        chunk_size (int): size of chunks."""
    k = len(x) // chunk_size
    for i in range(k+1):
        yield x[i*chunk_size:(i+1)*chunk_size]


def raw2fastas(raw):
    """Parse raw string into fastas.

    Args:
        raw (iterable): lines of raw fasta.
    Yield:
        fasta objects.
    """
    sequence = []
    for l in raw:
        l = l.replace('\n','')
        if l:
            if l[0] == '>':
                if sequence:
                    yield fasta(header, "".join(sequence))
                    sequence = []
                header = l
            else:
                sequence.append(l)
    if sequence:
        yield fasta(header, "".join(sequence))

class FastasAlreadyReversedError(Exception):
    pass


class Fastas(list):
    def read(self, path):
        """Append fastas from a file."""
        with open(path, 'r') as f:
            self.extend(raw2fastas(f))

    def parse(self, raw):
        """Parse a raw string containing some fasta sequences.

        Args:
            raw (str): a raw string with fasta file contents.
        """
        self.extend(raw2fastas(raw.splitlines()))

    def write(self, path, mode='w+', chunk_size=80):
        """Write file under the given path."""
        path = Path(path).expanduser().resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, mode) as h:
            for f in self:
                if chunk_size:
                    h.write(f.header + '\n')
                    for chunk in iter_chunks(f.sequence, chunk_size):
                        h.write(chunk + '\n')
                else:
                    h.write("{}\n{}\n".format(f.header, f.sequence))

    def download(self, url):
        """Append fastas found at a given url."""
        self.parse(download(url))

    def repeat_stats(self):
        """Get the distribution of shared fasta sequences."""
        return dict(Counter(Counter(f.sequence for f in self).values()))

    def any_reversed(self):
        return any("REVERSE" in f.header for f in self)

    def reverse(self):
        """Extend fastas by adding reversed sequences."""
        if not self.any_reversed():
            self.extend([f.reverse(i+1) for i,f in enumerate(self)])
        else:
            raise FastasAlreadyReversedError()

    def get_reversed(self):
        """Return a reversed copy of the fasta."""
        return Fastas(f.reverse(i+1) for i,f in enumerate(self))

    def __add__(self, other):
        """Sum fastas."""
        out = self.__class__()
        out.extend(self)
        out.extend(other)
        return out

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, len(self))

    def fasta_types(self):
        """Count occurences of different fastas."""
        return dict(Counter(f.__class__.__name__ for f in self))

    def same_fasta_types(self):
        """Check if all fastas are of the same type."""
        return len(self.fasta_types()) in (0,1)

    def download(self, url):
        """Download the query/species sequences from url."""
        self.parse(download(url))


def fastas(path_url, verbose=False):
    """Read in a fasta object from a given path.

    Args:
        path_url (str or pathlib.Path): Path to the fasta file or a valid url to where the fastas can be found.
    Returns:
        Fastas
    """
    fs = Fastas()
    try:
        fs.read(path_url)
    except (FileNotFoundError, OSError):
        if verbose:
            print('File missing, trying out a url.')
        fs.parse(download(path_url))
    return fs