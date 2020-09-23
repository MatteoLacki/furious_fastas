import pathlib
from pprint import pprint

from .fastas import fastas
from .contaminants import contaminants


def prepare_fasta_file(path, add_contaminants, reverse, verbose=False):
    """Cast fastas into NCBI general format, add contaminants and reverse.

    Args:
        path (str): Path to the fasta of interest.
        add_contaminants (boolean): should we add in standard contaminants?
        reverse (boolean): should we add in reversed sequences?
        verbose (boolean): be verbose?
    Returns:
        pathlib.Path: Path to the prepared fasta file.
    """
    path = pathlib.Path(path)
    fs = fastas(path)
    if verbose: print(f'These fastas consist of:\n{fs.fasta_types()}')
    if verbose: print('Translating to NCBI general fasta format.')
    fastas.to_ncbi_general()
    if add_contaminants: fs.extend(contaminants.to_ncbi_general())
    if reverse: fs.reverse()
    path = path.parent/f"{path.stem}{f'_contaminants_{len(contaminants)}' if add_contaminants else ''}{'_reversed' if reverse else ''}_pipelineFriendly.fasta"
    fs.write(path)
    return path


def fasta_path_gui(db):
    """Get path to the proper fasta file.

    The 

    Args:
        db (str): 
    """
    db = pathlib.Path(db)
    path = input('fastas to use (human|wheat|..|custom path): ')
    add_contaminants = input('Adding contaminants! Type in anything to stop me or hit ENTER:') == ''
    print(f"We will{'' if add_contaminants else ' not'} add contaminants to the fastas.")
    reverse = input('Reversing! Type in anything to stop me or hit ENTER:') == ''
    print(f"We will{'' if reverse else ' not'} reverse the fastas.")

    # anti-xor used
    pipelineFriendly = [p for p in db.glob("*_pipelineFriendly.fasta") if (p.stem.split('_',1)[0] == path) and (not reverse ^ ('reverse' in p.stem)) and (not add_contaminants ^ ('contaminants' in p.stem)) ]

    if len(pipelineFriendly) > 1:
        raise FileExistsError('There are too many files matchin the criteria in the DB.')
    
    if len(pipelineFriendly) == 1:
        print(f'We found your fasta in the data base:\n{pipelineFriendly[0]}')
        if input('Hit ENTER if OK. Otherwise submit a path now:') == '':
            return pipelineFriendly[0]
    else:
        path = pathlib.Path(path)
        assert path.exists(), "The provided path does not exist or is unreachable."
        print(f'Provided path is not in the data base:\n{path}')
        print('Preparing fastas.')
        return prepare_fasta_file(path, add_contaminants, reverse, True)
    
