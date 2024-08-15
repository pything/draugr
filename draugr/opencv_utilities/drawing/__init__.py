#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 14/01/2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .opencv_draw import *
from .opencv_drawing_utilities import *
from .draw_boxes import *
from .masks import *
