#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 14/01/2020
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md", "r") as this_init_file:
    __doc__ += this_init_file.read()

from .business import *
from .datetimes import *
from .debug import *
from .exceptions import *
from .manipulation import *
from .replication import *
from .sockets import *
from .styling import *
from .torch_like_channel_transformation import *
from .resource_utilities import *
from .platform_selection import *
from .strings import *
from .powers import *
from .contexts import *
from .path_utilities import *
from .function_wrappers import *
