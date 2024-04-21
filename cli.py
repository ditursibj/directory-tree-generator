import argparse
import pathlib
import sys

from _init_ import __version__
from directory_tree import DirectoryTree

def main():
    args = parse_cli_args()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print(f"'{root_dir}' does not exist")
        sys.exit()
    
    tree = DirectoryTree(root_dir=root_dir)
    tree.generate()

def parse_cli_args():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="Directory tree (DT) visualizer",
        epilog="Plant a tree!"
    )
    parser.version = f'DT version v{__version__}'
    # arg for version flag
    parser.add_argument('-v', '--version', action='version')
    # arg for root_dir flag
    parser.add_argument(
        'root_dir',
        metavar='ROOT_DIR',
        nargs='?',
        default='.',
        help='Generate a directory tree startign at ROOT_DIR'
    )
    return parser.parse_args()