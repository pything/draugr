#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/10/2023
           """

__all__ = ["positive_int_hash"]

import zlib
from typing import Optional

import numpy

MAX_INT_8 = numpy.iinfo(numpy.int8).max
MAX_INT_16 = numpy.iinfo(numpy.int16).max
MAX_INT_32 = numpy.iinfo(numpy.int32).max
MAX_INT_64 = numpy.iinfo(numpy.int64).max

MAX_UINT_8 = numpy.iinfo(numpy.uint8).max
MAX_UINT_16 = numpy.iinfo(numpy.uint16).max
MAX_UINT_32 = numpy.iinfo(numpy.uint32).max
MAX_UINT_64 = numpy.iinfo(numpy.uint64).max


def positive_int_hash(
    s: str, limit_size: Optional[int] = MAX_INT_32, hasher: callable = zlib.crc32
) -> int:
    """

    :param hasher:
    :param s:
    :param limit_size:
    :return:
    """
    pos_int = hasher(s.encode("utf-8")) & 0xFFFFFFFF
    if limit_size:  # Wrap around
        pos_int %= limit_size
    return pos_int


if __name__ == "__main__":
    for i in range(100):
        print(positive_int_hash(f"{i}"))
