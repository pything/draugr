#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from typing import Tuple

import numpy
import torch

__all__ = [
    "CV2ToImage",
    "CV2ToTensor",
]


class CV2ToImage:
    def __call__(
        self,
        tensor: torch.Tensor,
        boxes: numpy.ndarray = None,
        labels: numpy.ndarray = None,
    ) -> Tuple:
        return (
            tensor.cpu().numpy().astype(numpy.float32).transpose((1, 2, 0)),
            boxes,
            labels,
        )


class CV2ToTensor:
    def __call__(
        self,
        cvimage: numpy.ndarray,
        boxes: numpy.ndarray = None,
        labels: numpy.ndarray = None,
    ) -> Tuple:
        return (
            torch.from_numpy(cvimage.astype(numpy.float32)).permute(2, 0, 1),
            boxes,
            labels,
        )
