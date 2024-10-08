#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

import torch

__all__ = ["copy_parameters", "copy_state"]


def copy_parameters(
    target: torch.nn.Module, source: torch.nn.Module
) -> torch.nn.Module:
    """description"""
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(param.data)
    return target


def copy_state(*, target: torch.nn.Module, source: torch.nn.Module) -> torch.nn.Module:
    """description"""
    target.load_state_dict(source.state_dict())
    return target
