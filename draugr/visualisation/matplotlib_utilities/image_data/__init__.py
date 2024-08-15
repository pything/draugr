#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""
"""

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .display_3d_depth_image import *
from .display_depth_image import *
from .replay_frames import *
from .multiple import *
