#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from dataclasses import dataclass


@dataclass
class TemporalCommunityPost:
    title: str
    url: str
    views: int
