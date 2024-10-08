#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 27/06/2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .complexity import *
from .counting import *
from .freezing import *
from .initialisation import *
from .regularisation import *
from .trainable import *
from .exporting import *
from .differential_operators import *
