#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

__doc__ = r"""

           Created on 18/03/2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .tensorboard import *
from .torch_module_writer import *
from .mixins import *

# from .visdom import *
