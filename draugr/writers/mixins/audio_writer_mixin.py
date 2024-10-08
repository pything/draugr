#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Union

import numpy
import torch
from PIL import Image

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/10/2019
           """
__all__ = ["AudioWriterMixin"]


class AudioWriterMixin(ABC):
    """
    Writer subclass that provides an interface for 'writing' audio clips"""

    @abstractmethod
    def audio(
        self,
        tag: str,
        data: Union[numpy.ndarray, torch.Tensor, Image.Image],
        step,
        **kwargs
    ) -> None:
        """

        :param tag:
        :type tag:
        :param data:
        :type data:
        :param step:
        :type step:
        :param kwargs:
        :type kwargs:"""
        raise NotImplementedError
