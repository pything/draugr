#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 30-12-2020
           """

if __name__ == "__main__":
    from draugr.visualisation.progress import progress_bar

    for a in progress_bar(range(100)):
        print(a)
