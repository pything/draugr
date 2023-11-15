# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class TemporalCommunityPost:
    title: str
    url: str
    views: int
