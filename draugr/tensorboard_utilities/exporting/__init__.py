#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 17-03-2021
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# #del Path

from .event_export import *
from .file_export import *
from .db_export import *

if __name__ == "__main__":
    print(__doc__)
