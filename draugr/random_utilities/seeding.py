#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 11-12-2020
           """

import os
import random

__all__ = ["seed_stack"]


def seed_stack(s: int = 23) -> None:
    """description"""
    from draugr.torch_utilities import torch_seed

    python_seed(s)
    numpy_seed(s)
    torch_seed(s)


def python_seed(s: int = 2318) -> None:
    """description"""
    random.seed(s)
    os.environ["PYTHONHASHSEED"] = str(s)


def numpy_seed(s: int = 78213) -> None:
    """description"""
    import numpy

    numpy.random.seed(s)
