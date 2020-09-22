#!/usr/bin/env python3
import argparse
import pathlib

from furious_fastas.parse import parse_settings
from furious_fastas.update import update_plgs_peaks_fastas as update


resolve = lambda p: pathlib.Path(p).resolve()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Update fasta databases.')
    parser.add_argument("db_path",
        help="Path to the folder treated as database.",
        type=resolve)
    parser.add_argument("species2url_path",
        help="Path to the file mapping species names to urls.",
        type=resolve)
    a = parser.parse_args()
    update(db_path=a.db_path,
           species2url=parse_settings(a.species2url_path),
           verbose=True)