#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 01/03/2020
           """

from abc import abstractmethod
from typing import Dict, Tuple

from torch.utils.data import Dataset

__all__ = ["SupervisedDataset"]

from draugr.numpy_utilities.datasets.splitting import (
    SplitEnum,
    SplitIndexer,
)
from warg import drop_unused_kws


class SupervisedDataset(Dataset):
    """
    Supervised Dataset comprises separate Splits"""

    @drop_unused_kws
    def __init__(self):
        pass

    @property
    def split_names(self) -> Dict[SplitEnum, str]:
        """

        :return:
        :rtype:"""
        return SplitIndexer.default_split_names

    @property
    @abstractmethod
    def response_shape(self) -> Tuple[int, ...]:
        """description"""
        raise NotImplementedError

    @property
    @abstractmethod
    def predictor_shape(self) -> Tuple[int, ...]:
        """description"""
        raise NotImplementedError

    @abstractmethod
    def __len__(self):
        raise NotImplementedError

    @abstractmethod
    def __getitem__(self, index: int):
        raise NotImplementedError
