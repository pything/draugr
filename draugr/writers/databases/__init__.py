#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 9/14/19
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .hdf_writer import *
from .sqlite_writer import *
