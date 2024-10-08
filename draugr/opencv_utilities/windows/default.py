#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from enum import Enum
from typing import Iterable

from sorcery import assigned_names

__all__ = ["ExtensionEnum", "match_return_code"]

ESC_CHAR = chr(27)


def match_return_code(ret_val, chars: Iterable[str] = ("q", ESC_CHAR)) -> bool:
    """

    :param ret_val:
    :type ret_val:
    :param chars:
    :type chars:
    :return:
    :rtype:
    """
    if ret_val:
        return any(ret_val & 0xFF == ord(c) for c in chars)
    return False


class ExtensionEnum(Enum):
    png, exr = assigned_names()
