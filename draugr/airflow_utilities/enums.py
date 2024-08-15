#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

__doc__ = r"""
"""
from enum import Enum

from sorcery import assigned_names

__all__ = ["AutoRemoveEnum"]


class AutoRemoveEnum(Enum):
    never, success, force = assigned_names()
