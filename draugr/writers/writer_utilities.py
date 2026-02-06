from typing import Dict

import numpy

__author__ = "Christian Heider Lindbjerg"
__doc__ = """
Created on 27/04/2019

@author: cnheider
"""

__all__ = ["metrics"]


def metrics(array: numpy.ndarray) -> Dict:
    """

    :param array:
    :type array:
    :return:
    :rtype:"""
    d = {
        "mean": numpy.mean(array),
        "std": numpy.std(array),
        "min": numpy.amin(array),
        "max": numpy.amax(array),
    }
    return d
