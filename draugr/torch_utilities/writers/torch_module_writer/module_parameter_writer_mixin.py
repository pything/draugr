#!/usr/bin/env python3
from abc import ABC, abstractmethod

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/10/2019
           """
__all__ = ["ModuleParameterWriterMixin"]

import torch


class ModuleParameterWriterMixin(ABC):
    """
    Writer mixin that provides an interface for 'writing' torch Module parameters"""

    @abstractmethod
    def parameters(self, tag: str, model: torch.nn.Module, step: int, **kwargs) -> None:
        """
        Write Module parameters

        :param tag:
        :type tag:
        :param model:
        :type model:
        :param step:
        :type step:
        :param kwargs:
        :type kwargs:"""
        raise NotImplementedError
