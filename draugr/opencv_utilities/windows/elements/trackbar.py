#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from typing import Callable, Optional

import cv2

from warg import Number, sink

__all__ = ["add_trackbar"]


def add_trackbar(
    window_name: str,
    trackbar_name: str,
    default: Optional[Number] = None,
    *,
    min_val: Number = 0,
    max_val: Number = 255,
    callback: Callable = sink
) -> None:
    """
    Adds a trackbar to a window.
    :param default:
    :type default:
    :param min_val:
    :type min_val:
    :param max_val:
    :type max_val:
    :param window_name: Name of the window to add the trackbar to.
    :param trackbar_name: Name of the trackbar.
    :param callback: Callback function to be called when the trackbar is moved.
    :return: None
    """
    if default is None:
        default = min_val + (max_val - min_val) // 2
    default = int(default)
    min_val = int(min_val)
    max_val = int(max_val)
    cv2.createTrackbar(trackbar_name, window_name, default, max_val, callback)
    # cv2.setTrackbarPos(trackbar_name, window_name, default)
    cv2.setTrackbarMin(trackbar_name, window_name, min_val)
    # cv2.setTrackbarMax(trackbar_name, window_name, max_val)
