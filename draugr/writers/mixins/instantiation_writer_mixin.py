#!/usr/bin/env python3
from abc import ABC, abstractmethod

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/10/2019
           """
__all__ = ["InstantiationWriterMixin"]

from typing import Mapping

from warg import drop_unused_kws


class InstantiationWriterMixin(ABC):
    """
    Writer mixin that provides an interface for 'writing' instantiation"""

    @drop_unused_kws
    @abstractmethod
    def instance(self, instance: Mapping, metrics: Mapping) -> None:
        """description"""
        raise NotImplementedError
