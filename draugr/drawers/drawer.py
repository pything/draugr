#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 25-01-2021
           """

__all__ = ["Drawer"]

from abc import abstractmethod
from typing import Any, MutableMapping, Sequence

from warg import drop_unused_kws


class Drawer:
    """
    Abstract class for drawing representations of data
    """

    @drop_unused_kws
    def __init__(self, verbose: bool = False):
        self._verbose = verbose

    @abstractmethod
    def draw(self, *args: Sequence[Any], **kwargs: MutableMapping[str, Any]) -> None:
        """description"""
        raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
