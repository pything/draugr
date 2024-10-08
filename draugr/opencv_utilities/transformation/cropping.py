#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from typing import Sequence

import cv2
import numpy

__all__ = ["circle_crop"]


def circle_crop(image: numpy.ndarray, center: Sequence, radius: int) -> numpy.ndarray:
    """
    Return a circle crop of the image at given center with given radius

    :param image:
    :type image:
    :param center:
    :type center:
    :param radius:
    :type radius:
    :return:
    :rtype:
    """
    mask = numpy.zeros(image.shape[:2], dtype="uint8")
    cv2.circle(mask, center, radius, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    cropped = masked[
        center[1] - radius : center[1] + radius + 1,
        center[0] - radius : center[0] + radius + 1,
    ]

    return cropped
