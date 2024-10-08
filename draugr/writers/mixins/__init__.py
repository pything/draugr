#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 05/07/2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md") as this_init_file:
    __doc__ += this_init_file.read()
# del Path

from .bar_writer_mixin import *
from .embed_writer_mixin import *
from .figure_writer_mixin import *
from .histogram_writer_mixin import *
from .image_writer_mixin import *
from .line_writer_mixin import *
from .spectrogram_writer_mixin import *
from .precision_recall_writer_mixin import *
from .audio_writer_mixin import *
from .instantiation_writer_mixin import *
from .video_writer_mixin import *
from .mesh_writer_mixin import *
from .scalar_writer_mixin import *
