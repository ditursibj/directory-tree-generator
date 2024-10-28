import os
import pathlib

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class DirectoryTree:
    """
    Display the diagram.

    Args: None.

    Returns:
        A printed entry.
    """

    def __init__(self, root_dir: str) -> str:
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)

class _TreeGenerator:
    """
    Traverse the file system and generate the directory tree diagram.

    Args: None.

    Returns:
        Directory tree.
    """
   
    # Turn root_dir into a pathlib.Path object
    def __init__(self, root_dir: str) -> None:
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    # Public method to generate and return the tree diagram
    def build_tree(self) -> list:
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    
    # Add the name of _root_dir to ._tree
    def _tree_head(self) -> None:
        self._tree.append(f'{self._root_dir}{os.sep}')
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):
        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)

        for index, entry in enumerate(entries):
            connector = ELBOW if index ==entries_count - 1 else TEE
            if entry.is_dir():
                self._add_directory(entry, index,entries_count, prefix, connector)
            else:
                self._add_file(entry, prefix, connector)
    
    def _add_directory(self, directory,index, entries_count, prefix, connector):
        self._tree.append(f'{prefix}{connector} {directory.name}{os.sep}')
        
        if index != entries_count -1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        
        self._tree_body(directory=directory, prefix=prefix)

    def _add_file(self, file, prefix, connector):
        self._tree.append(f'{prefix}{connector} {file.name}')
