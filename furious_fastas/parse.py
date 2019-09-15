def parse_settings(path):
    """Parse the settings file.

    Arguments:
        path (str): Path to the files.
        prepend (str): What is prepended to the url (like most of it).
    Yields:
        tuple : name and a tuple with urls to download and concatenate.
    """
    with open(path, 'r') as f:
        for l in f:
            l = l.split()
            name = l[0]
            urls = tuple(l[1:])
            yield name, urls
