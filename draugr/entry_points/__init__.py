#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 9/5/19
           """

from pathlib import Path

with open(Path(__file__).parent / "README.md", "r") as this_init_file:
    __doc__ += this_init_file.read()
# del Path
