#!/usr/bin/env python3
__author__ = "Christian Heider Lindbjerg"

__doc__ = r"""
"""

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .config import *
from .model import *
from .parameters import *
from .naming import *
from .checkpoint import *
