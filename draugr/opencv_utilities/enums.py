#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "heider"
__doc__ = r"""

           Created on 01/02/2022
           """

__all__ = [
    "MarkerTypesEnum",
    "DistanceTypesEnum",
    "ThresholdTypeFlag",
    "HoughModeEnum",
    "WindowFlagEnum",
    "WindowPropertyFlag",
    "ContourRetrievalModeEnum",
    "MouseEventEnum",
    "MouseEventFlag",
    "FontEnum",
]

from enum import Enum, Flag

import cv2


class MarkerTypesEnum(Enum):
    cross = cv2.MARKER_CROSS  # A crosshair marker shape.
    tilted_cross = cv2.MARKER_TILTED_CROSS  # A 45 degree tilted crosshair marker shape.
    star = (
        cv2.MARKER_STAR
    )  # A star marker shape, combination of cross and tilted cross.
    diamond = cv2.MARKER_DIAMOND  # A diamond marker shape.
    square = cv2.MARKER_SQUARE  # A square marker shape.
    triangle_up = cv2.MARKER_TRIANGLE_UP  # An upwards pointing triangle marker shape.
    triangle_down = (
        cv2.MARKER_TRIANGLE_DOWN
    )  # A downwards pointing triangle marker shape.


class DistanceTypesEnum(Enum):
    user = cv2.DIST_USER  # User defined distance.
    l1 = cv2.DIST_L1  # distance = |x1-x2| + |y1-y2|
    l2 = cv2.DIST_L2  # the simple euclidean distance
    c = cv2.DIST_C  # distance = max(|x1-x2|,|y1-y2|)
    l12 = cv2.DIST_L12  # L1-L2 metric: distance = 2(sqrt(1+x*x/2) - 1))
    fair = cv2.DIST_FAIR  # distance = c^2(|x|/c-log(1+|x|/c)), c = 1.3998
    welsch = cv2.DIST_WELSCH  # distance = c^2/2(1-exp(-(x/c)^2)), c = 2.9846
    huber = cv2.DIST_HUBER  # distance = |x|<c ? x^2/2 : c(|x|-c/2), c=1.345


class DistanceTransformLabelTypesEnum(Enum):
    """
    distanceTransform algorithm flags
    """

    ccomp = cv2.DIST_LABEL_CCOMP
    """each connected component of zeros in src (as well as all the non-zero pixels closest to the connected component) will be assigned the same label
"""

    pixel = cv2.DIST_LABEL_PIXEL
    """each zero pixel (and all the non-zero pixels closest to it) gets its own label."""


class DistanceTransformMasksEnum(Enum):
    """
    Mask size for distance transform.
    """

    mask_3 = cv2.DIST_MASK_3
    mask_5 = cv2.DIST_MASK_5
    mask_precise = cv2.DIST_MASK_PRECISE


class ThresholdTypeFlag(Flag):
    binary = cv2.THRESH_BINARY  # dst(x,y)={maxval0if src(x,y)>threshotherwise
    inverse_binary = (
        cv2.THRESH_BINARY_INV
    )  # dst(x,y)={0maxvalif src(x,y)>threshotherwise
    truncate = (
        cv2.THRESH_TRUNC
    )  # dst(x,y)={thresholdsrc(x,y)if src(x,y)>threshotherwise
    to_zero = cv2.THRESH_TOZERO  # dst(x,y)={src(x,y)0if src(x,y)>threshotherwise
    inverse_to_zero = (
        cv2.THRESH_TOZERO_INV
    )  # dst(x,y)={0src(x,y)if src(x,y)>threshotherwise
    mask = cv2.THRESH_MASK
    otsu = (
        cv2.THRESH_OTSU
    )  # flag, use Otsu algorithm to choose the optimal threshold value
    triangle = (
        cv2.THRESH_TRIANGLE
    )  # flag, use Triangle algorithm to choose the optimal threshold value


class TermCriteriaEnum(Flag):
    count = (
        cv2.TERM_CRITERIA_COUNT
    )  # the maximum number of iterations or elements to compute
    eps = (
        cv2.TERM_CRITERIA_EPS
    )  # the desired accuracy or change in parameters at which the iterative algorithm stops
    max_iter = cv2.TERM_CRITERIA_MAX_ITER  # the maximum number of iterations to compute


class KmeansEnum(Enum):
    random_centers = (
        cv2.KMEANS_RANDOM_CENTERS
    )  # Select random initial centers in each attempt.
    pp_centers = (
        cv2.KMEANS_PP_CENTERS
    )  # Use kmeans++ center initialization by Arthur and Vassilvitskii [Arthur2007].
    use_initial_labels = (
        cv2.KMEANS_USE_INITIAL_LABELS
    )  # During the first (and possibly the only) attempt, use the user-supplied labels instead of computing them from the initial centers. For the second and further attempts, use the random or semi-random centers. Use one of KMEANS_*_CENTERS flag to specify the exact method.


class HoughModeEnum(Enum):
    standard = (
        cv2.HOUGH_STANDARD
    )  # classical or standard Hough transform. Every line is represented by two floating-point numbers (ρ,θ) , where ρ is a distance between (0,0) point and the line, and θ is the angle between x-axis and the normal to the line. Thus, the matrix must be (the created sequence will be) of CV_32FC2 type
    gradient = cv2.HOUGH_GRADIENT  # basically 21HT
    probabilistic = (
        cv2.HOUGH_PROBABILISTIC
    )  # probabilistic Hough transform (more efficient in case if the picture contains a few long linear segments). It returns line segments rather than the whole line. Each segment is represented by starting and ending points, and the matrix must be (the created sequence will be) of the CV_32SC4 type.
    multi_scale = (
        cv2.HOUGH_MULTI_SCALE
    )  # multi-scale variant of the classical Hough transform. The lines are encoded the same way as HOUGH_STANDARD.
    gradient_alternative = (
        cv2.HOUGH_GRADIENT_ALT
    )  # variation of HOUGH_GRADIENT to get better accuracy


class WindowFlagEnum(Enum):
    normal = (
        cv2.WINDOW_NORMAL
    )  # the user can resize the window (no constraint) / also use to switch a fullscreen window to a normal size.
    autosize = (
        cv2.WINDOW_AUTOSIZE
    )  # the user cannot resize the window, the size is constrainted by the image displayed.
    opengl = cv2.WINDOW_OPENGL  # window with opengl support.
    fullscreen = cv2.WINDOW_FULLSCREEN  # change the window to fullscreen.
    free_ratio = (
        cv2.WINDOW_FREERATIO
    )  # the image expends as much as it can (no ratio constraint).
    keep_ratio = cv2.WINDOW_KEEPRATIO  # the ratio of the image is respected.
    gui_expanded = cv2.WINDOW_GUI_EXPANDED  # status bar and tool bar
    gui_normal = cv2.WINDOW_GUI_NORMAL  # old fashious way


class MorphShapesEnum(Enum):
    rect = cv2.MORPH_RECT  # a rectangular structuring element: Eij=1
    cross = (
        cv2.MORPH_CROSS
    )  # a cross-shaped structuring element: Eij={10if i=anchor.y or j=anchor.x otherwise
    ellipse = (
        cv2.MORPH_ELLIPSE
    )  # an elliptic structuring element, that is, a filled ellipse inscribed into the rectangle Rect(0, 0, esize.width, 0.esize.height)


class MorphTypesEnum(Enum):
    erode = cv2.MORPH_ERODE
    dilate = cv2.MORPH_DILATE
    open = cv2.MORPH_OPEN  # dst=open(src,element)=dilate(erode(src,element))
    close = cv2.MORPH_CLOSE  # dst=close(src,element)=erode(dilate(src,element))
    gradient = (
        cv2.MORPH_GRADIENT
    )  # dst=morph_grad(src,element)=dilate(src,element)−erode(src,element)
    tophat = cv2.MORPH_TOPHAT  # dst=tophat(src,element)=src−open(src,element)
    blackhat = cv2.MORPH_BLACKHAT  # dst=blackhat(src,element)=close(src,element)−src
    hitmiss = cv2.MORPH_HITMISS  # Only supported for CV_8UC1 binary images.


class WindowPropertyFlag(Flag):
    fullscreen = (
        cv2.WND_PROP_FULLSCREEN
    )  # fullscreen property (can be WINDOW_NORMAL or WINDOW_FULLSCREEN).
    autosize = (
        cv2.WND_PROP_AUTOSIZE
    )  # autosize property (can be WINDOW_NORMAL or WINDOW_AUTOSIZE).
    keep_ratio = (
        cv2.WND_PROP_ASPECT_RATIO
    )  # window's aspect ration (can be set to WINDOW_FREERATIO or WINDOW_KEEPRATIO).
    opengl = cv2.WND_PROP_OPENGL  # opengl support.
    visible = cv2.WND_PROP_VISIBLE  # checks whether the window exists and is visible
    topmost = (
        cv2.WND_PROP_TOPMOST
    )  # property to toggle normal window being topmost or not


class FontEnum(Enum):
    hershey_simplex = cv2.FONT_HERSHEY_SIMPLEX  # normal size sans-serif font

    hershey_plain = cv2.FONT_HERSHEY_PLAIN  # small size sans-serif font

    hershey_duplex = (
        cv2.FONT_HERSHEY_DUPLEX
    )  # normal size sans-serif font (more complex than FONT_HERSHEY_SIMPLEX)

    hershey_complex = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font

    hershey_triplex = (
        cv2.FONT_HERSHEY_TRIPLEX
    )  # normal size serif font (more complex than FONT_HERSHEY_COMPLEX)

    hershey_complex_small = (
        cv2.FONT_HERSHEY_COMPLEX_SMALL
    )  # smaller version of FONT_HERSHEY_COMPLEX

    hershey_script_simplex = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # hand-writing style font

    hershey_script_complex = (
        cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    )  # more complex variant of FONT_HERSHEY_SCRIPT_SIMPLEX

    italic = cv2.FONT_ITALIC  # flag for italic font


class ContourRetrievalModeEnum(Enum):
    """

      RETR_EXTERNAL retrieves only the extreme outer contours. It sets hierarchy[i][2]=hierarchy[i][3]=-1 for all the contours.
    RETR_LIST retrieves all of the contours without establishing any hierarchical relationships.
    RETR_CCOMP retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components. At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.
    RETR_TREE retrieves all of the contours and reconstructs a full hierarchy of nested contours. This full hierarchy is built and shown in the OpenCV contours.c demo.

      :return:
      :rtype:
    """

    external = cv2.RETR_EXTERNAL
    list_all = cv2.RETR_LIST
    ccomp = cv2.RETR_CCOMP
    tree = cv2.RETR_TREE


class MouseEventEnum(Enum):
    move = (
        cv2.EVENT_MOUSEMOVE
    )  # indicates that the mouse pointer has moved over the window.
    left_down = (
        cv2.EVENT_LBUTTONDOWN
    )  # indicates that the left mouse button is pressed.
    left_up = cv2.EVENT_LBUTTONUP  # indicates that left mouse button is released.
    left_double = (
        cv2.EVENT_LBUTTONDBLCLK
    )  # indicates that left mouse button is double clicked.
    right_down = (
        cv2.EVENT_RBUTTONDOWN
    )  # indicates that the right mouse button is pressed.
    right_up = cv2.EVENT_RBUTTONUP  # indicates that right mouse button is released.
    right_double = (
        cv2.EVENT_RBUTTONDBLCLK
    )  # indicates that right mouse button is double clicked.
    middle_down = (
        cv2.EVENT_MBUTTONDOWN
    )  # indicates that the middle mouse button is pressed.
    middle_up = cv2.EVENT_MBUTTONUP  # indicates that middle mouse button is released.
    middle_double = (
        cv2.EVENT_MBUTTONDBLCLK
    )  # indicates that middle mouse button is double clicked.
    wheel_ud = (
        cv2.EVENT_MOUSEWHEEL
    )  # positive and negative values mean forward and backward scrolling, respectively.
    wheel_rl = (
        cv2.EVENT_MOUSEHWHEEL
    )  # positive and negative values mean right and left scrolling, respectively.


class MouseEventFlag(Flag):
    ctrl_down = cv2.EVENT_FLAG_CTRLKEY  # indicates that CTRL Key is pressed.
    shift_down = cv2.EVENT_FLAG_SHIFTKEY  # indicates that SHIFT Key is pressed.
    alt_down = cv2.EVENT_FLAG_ALTKEY  # indicates that ALT Key is pressed.
    left_down = cv2.EVENT_FLAG_LBUTTON  # indicates that the left mouse button is down.
    right_down = (
        cv2.EVENT_FLAG_RBUTTON
    )  # indicates that the right mouse button is down.
    middle_down = (
        cv2.EVENT_FLAG_MBUTTON
    )  # indicates that the middle mouse button is down.
