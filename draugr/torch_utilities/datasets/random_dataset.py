#!/usr/bin/env python3
from typing import Any, Sequence

import torch
from torch.utils.data import Dataset

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 09/10/2019
           """

__all__ = ["RandomDataset"]


class RandomDataset(Dataset):
    """Random dataset on instantiation"""

    def __init__(self, nd_size: Sequence, length: int):
        self.len = length
        self.data = torch.randn((length, *nd_size))

    def __getitem__(self, index: int) -> Any:
        return self.data[index]

    def __len__(self):
        return self.len


if __name__ == "__main__":
    print(RandomDataset((5, 5), 10)[0])
