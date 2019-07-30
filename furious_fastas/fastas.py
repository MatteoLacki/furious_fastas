"""Classes representing collections of fastas."""
from collections import Counter

from .parse import parse_uniprot_fastas, parse_ncbi_general_fastas
from .fasta import Fasta


class Fastas(list):
    def read(self, path):
        """Append fastas from a file."""
        with open(path, 'r') as f:
            raw = f.read()
        self.parse(raw) 

    def parse(self, raw):
        """Parse a raw string containing some fasta sequences."""
        all_lines = raw.splitlines()
        headers = []
        headers_idx = []
        for i, l in enumerate(all_lines):
            if l[0] == '>':
                headers.append(l)
                headers_idx.append(i)
        headers_idx.append(len(all_lines))
        headers_idx = iter(headers_idx)
        prev_idx = next(headers_idx) + 1
        for next_idx, header in zip(headers_idx, headers):
            sequence = "".join(all_lines[prev_idx:next_idx])
            self.append(Fasta(sequence, header))
            prev_idx = next_idx + 1

    def write(self, path, mode='w+'):
        """Write file under the given path."""
        with open(path, mode) as h:
            for f in self:
                h.write("{}\n{}\n".format(f.header, f.sequence))

    def repeat_stats(self):
        """Get the distribution of shared fasta sequences."""
        return dict(Counter(Counter(f.sequence for f in self).values()))

    def reverse(self):
        """Extend fastas by adding reversed sequences."""
        self.extend([f.reverse() for f in self])

    def __add__(self, other):
        """Sum fastas."""
        out = self.__class__()
        out.extend(self)
        out.extend(other)
        return out

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, len(self))



# class UniprotFastas(Fastas):
#     def parse_raw(self, raw):
#         """Parse a raw string.

#         Arguments:
#             raw (str): a string with fastas in.
#         """
#         self.fastas.extend(parse_uniprot_fastas(raw))

#     def to_ncbi_general(self):
#         other = NCBIgeneralFastas()
#         for f in self.fastas:
#             other.fastas.append(f.to_gnl())
#         return other


# class NCBIgeneralFastas(Fastas):
#     def read(self, path):
#         """Read the fastas from a file.

#         Args:
#             path (str): path to the file.
#         """
#         with open(path, 'r') as f:
#             raw = f.read()
#         self.parse_raw(raw)

#     def parse_raw(self, raw):
#         self.fastas.extend(parse_ncbi_general_fastas(raw))

#     def add_reversed_fastas_for_plgs(self):
#         for i in range(len(self.fastas)):
#             self.fastas.append(self.fastas[i].reverse_for_plgs(i+1))