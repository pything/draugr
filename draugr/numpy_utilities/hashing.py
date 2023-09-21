__all__ = ["positive_int_hash"]

import zlib

import numpy

MAX_INT_32 = numpy.iinfo(numpy.int32).max


def positive_int_hash(s: str, limit_size=MAX_INT_32) -> int:
    pos_int = zlib.adler32(s.encode("utf-8")) & 0xFFFFFFFF
    if limit_size:  # Wrap around
        pos_int %= limit_size
    return pos_int
