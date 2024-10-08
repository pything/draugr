#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from enum import Enum
from typing import MutableMapping

import cv2
import numpy
from sorcery import assigned_names

__all__ = ["threshold_channel", "ThresholdMethodEnum", "hsv_min_max_clip_mask"]

from draugr.opencv_utilities.namespaces.flags import ThresholdTypeFlag
from draugr.opencv_utilities.namespaces.color_conversion_enum import ColorConversionEnum


class ThresholdMethodEnum(Enum):
    simple, adaptive = assigned_names()


def threshold_channel(
    gray: numpy.ndarray,
    method: ThresholdMethodEnum = ThresholdMethodEnum.simple,
    **kwargs: MutableMapping
) -> numpy.ndarray:
    """

    :param gray:
    :type gray:
    :param method:
    :type method:
    :param kwargs:
    :type kwargs:
    :return:
    :rtype:
    """
    method = ThresholdMethodEnum(method)

    if method == ThresholdMethodEnum.simple:
        return cv2.threshold(
            gray,
            thresh=kwargs.get("thresh", 120),
            maxval=kwargs.get("maxval", 255),
            type=ThresholdTypeFlag.otsu.value
            + ThresholdTypeFlag.binary.value,  # +ThresholdTypeFlag.to_zero.value,
        )[1]
    elif method == ThresholdMethodEnum.adaptive:
        return cv2.adaptiveThreshold(
            gray,
            maxValue=kwargs.get("maxValue", 255),
            adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            thresholdType=cv2.THRESH_BINARY,
            blockSize=11,
            C=2,
        )
    raise NotImplementedError


def hsv_min_max_clip_mask(
    input_image: numpy.ndarray,
    lower_bound: numpy.ndarray = numpy.array([0, 0, 0]),
    upper_bound: numpy.ndarray = numpy.array(
        [179, 255, 255]
    ),  # Hue is from 0-179 for Opencv
) -> numpy.ndarray:
    """

    :param input_image:
    :type input_image:
    :param lower_bound:
    :type lower_bound:
    :param upper_bound:
    :type upper_bound:
    :return:
    :rtype:
    """
    return cv2.inRange(
        cv2.cvtColor(input_image, ColorConversionEnum.bgr2hsv.value),
        lowerb=lower_bound,
        upperb=upper_bound,
    )
