#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 25-05-2021
           """

from pathlib import Path

try:
    from .formatting import *
    from .from_dict import *
    from .latex_mean_std import *
    from .misc_utilities import *
    from .multi_index_utilities import *
    from .styling import *
except ImportError as ix:
    this_package_name = Path(__file__).parent.name
    this_package_reqs = (
        Path(__file__).parent.parent.parent
        / "requirements"
        / f"requirements_{this_package_name}.txt"
    )
    if this_package_reqs.exists():
        print(
            f"Make sure requirements is installed for {this_package_name}, see {this_package_reqs}"
        )  # TODO: PARSE WHAT is missing and print
    raise ix
