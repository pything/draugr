#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""
"""

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

import warnings

warnings.filterwarnings(
    "ignore", category=FutureWarning
)  # Because Tensorflow needs to remind everyone all
# the time that their system is constantly being deprecated..
from .launcher import *
from .tensorboard_pytorch_writer import *

# from .tensorboard_x_writer import *
