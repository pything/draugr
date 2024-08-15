#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

__doc__ = r"""
"""

from enum import Enum

from sorcery import assigned_names

__all__ = [
    "PilModesEnum",
]


class PilModesEnum(Enum):
    """
      PIL pixel formats:

    RGB 24bits per pixel, 8-bit-per-channel RGB), 3 channels
    RGBA (8-bit-per-channel RGBA), 4 channels
    RGBa (8-bit-per-channel RGBA, remultiplied alpha), 4 channels
    1 - 1bpp, often for masks, 1 channel
    L - 8bpp, grayscale, 1 channel
    P - 8bpp, paletted, 1 channel
    I - 32-bit integers, grayscale, 1 channel
    F - 32-bit floats, grayscale, 1 channel
    CMYK - 8 bits per channel, 4 channels
    YCbCr - 8 bits per channel, 3 channels
    """

    OneBpp = "1"
    CMYK, F, HSV, I, L, LAB, P, RGB, RGBA, RGBX, YCbCr = assigned_names()
