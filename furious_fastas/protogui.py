import pathlib
from pprint import pprint

from .fastas import fastas
from .contaminants import contaminants



def prepare_fasta_file(path,
                       add_contaminants=True,
                       reverse=True, 
                       pipelineFriendly=True,
                       verbose=False):
    """Cast fastas into NCBI general format, add contaminants and reverse.

    Args:
        path (str): Path to the fasta of interest.
        add_contaminants (boolean): should we add in standard contaminants?
        reverse (boolean): should we add in reversed sequences?
        pipelineFriendly (boolean): translate fastas to General NCBI format?
        verbose (boolean): be verbose?
    Returns:
        pathlib.Path: Path to the prepared fasta file.
    """
    path = pathlib.Path(path)
    fs = fastas(path)
    if verbose:
        print(f'These fastas consist of:\n{fs.fasta_types()}')
    
    if add_contaminants:
        if verbose:
            print('Adding contaminants.')
        fs.extend(contaminants.to_ncbi_general())
    
    if pipelineFriendly:
        if verbose:
            print('Translating to NCBI general fasta format.')
        fs = fs.to_ncbi_general()

    if reverse:
        if verbose:
            print('Reversing')
        fs.reverse()
    
    path = path.parent/f"{path.stem}{f'_contaminants_{len(contaminants)}' if add_contaminants else ''}{'_reversed' if reverse else ''}{'_pipelineFriendly' if pipelineFriendly else ''}.fasta"
    
    if verbose:
        print(f"Saving the 'pipeline friendly' fasta under:\n{path}")
    fs.write(path)

    return path



def check_updated_fastas_folder(folder):
    try:
        folder = pathlib.Path(folder).expanduser().resolve()
    except TypeError:
        raise FileExistsError(f"Folder does not exist.")
    if not folder.exists() or not folder.is_dir():
        raise FileExistsError(f"Folder '{folder}' does not exist.")
    return folder



def get_pipeline_fasta_path(path_or_tag, add_contaminants, reverse,
                            updated_fastas_folder=None,
                            verbose=False):
    try:
        path_or_tag_PATH = pathlib.Path(path_or_tag).expanduser().resolve()
    except TypeError:
            raise FileExistsError("This path does not exist.")

    if path_or_tag_PATH.exists() and path_or_tag_PATH.is_file():
        path = path_or_tag_PATH
        return prepare_fasta_file(path, add_contaminants, reverse, 
                                  pipelineFriendly=True,
                                  verbose=verbose)

    tag = path_or_tag
    updated_fastas_folder = check_updated_fastas_folder(updated_fastas_folder)

    # anti-xor used
    pipelineFriendly = [p for p in updated_fastas_folder.glob("*/*_pipelineFriendly.fasta") if (p.stem.split('_',1)[0] == tag) and (not reverse ^ ('reverse' in p.stem)) and (not add_contaminants ^ ('contaminants' in p.stem)) ]

    if len(pipelineFriendly) > 1:
        raise FileExistsError('There are too many files matchin the criteria in the DB.')
    
    if len(pipelineFriendly) == 1:
        return pipelineFriendly[0]

    raise FileExistsError(f"Tag '{path_or_tag_PATH}' does not exist in {updated_fastas_folder}.")



def fasta_path_gui(updated_fastas_folder=None):
    """Get path to the proper fasta file.
 
    Args:
        updated_fastas_folder (str): path with data base. 
    """
    try:
        updated_fastas_folder = check_updated_fastas_folder(updated_fastas_folder)
        print("Write in or drag'n'drop a path from the explorer.")
        prompt = 'fastas to use (human|wheat|..|custom path): '
    except FileExistsError:
        prompt = "Drag'n'drop custom fasta file: "
    path_or_tag = input(prompt) or None

    add_contaminants = input('\nAdding contaminants! Type in anything to stop me or hit ENTER:') == ''
    print(f"We will{'' if add_contaminants else ' not'} add contaminants to the fastas.")
    reverse = input('\nReversing fastas. Type in anything to stop me or hit ENTER:') == ''
    print(f"We will{'' if reverse else ' not'} reverse the fastas.")

    return path_or_tag, updated_fastas_folder, add_contaminants, reverse

