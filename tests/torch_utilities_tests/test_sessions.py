#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 11/05/2020
           """

import torch

from warg import ensure_in_sys_path, find_nearest_ancestral_relative

ensure_in_sys_path(find_nearest_ancestral_relative("draugr").parent)
from draugr.torch_utilities import (
    TorchCpuSession,
    TorchCudaSession,
    TorchEvalSession,
    TorchTrainSession,
    global_torch_device,
)


def test_cpu():
    print(global_torch_device(override=global_torch_device(device_preference=True)))
    print(global_torch_device())
    with TorchCpuSession():
        print(global_torch_device())
    print(global_torch_device())


def test_nested_model_sessions():
    model = torch.nn.Sequential(torch.nn.Linear(1, 1), torch.nn.Dropout(0.1))
    print(model.training)
    with TorchEvalSession(model):
        print(model.training)
        with TorchTrainSession(model):
            print(model.training)
            with TorchEvalSession(model):
                print(model.training)
                with TorchTrainSession(model):
                    print(model.training)
                    with TorchEvalSession(model):
                        print(model.training)
    print(model.training)


def test_nested_device_sessions():
    print(global_torch_device(override=global_torch_device(device_preference=True)))
    print(global_torch_device())
    with TorchCpuSession():
        print(global_torch_device())
        with TorchCudaSession():
            print(global_torch_device())
            with TorchCpuSession():
                print(global_torch_device())
    print(global_torch_device())
