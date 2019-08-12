def parse_settings(path):
    """Parse the settings file.

    Arguments:
        path (str): Path to the files.
        prepend (str): What is prepended to the url (like most of it).
    Yields:
        tuple : name and full url of the species.
    """
    with open(path, 'r') as f:
        for l in f:
            name, url = l.split()
            yield name, url