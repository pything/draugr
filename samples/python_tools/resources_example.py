#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 08-12-2020
           """

import os

import psutil

process = psutil.Process(os.getpid())
print(process.memory_percent())
