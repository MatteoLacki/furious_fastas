from furious_fastas.fastas import Contaminants, Fastas, save_fastas
from furious_fastas.uniprot import uniprot

def update_factory(species):
    assert species in uniprot, "The name of species must be a key in the uniprot dict."
    def update(out_path):
        """Update fastas.

        Arguments
        =========
        out_path : str
            A path where the merged fastas should be saved as one bigger fasta file.
        """
        fastas = Fastas()
        fastas.download_from_uniprot(species)
        contaminants = Contaminants()
        save_fastas([fastas, contaminants], out_path)
    return update


# typical specifications.
human = update_factory("human")
ecoli = update_factory("ecoli")
wheat = update_factory("wheat")
mouse = update_factory("mouse")
yeast = update_factory("yeast")
leishmania = update_factory("leishmania")
