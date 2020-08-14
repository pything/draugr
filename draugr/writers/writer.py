#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = """
Created on 27/04/2019

@author: cnheider
"""

from abc import ABCMeta, abstractmethod
from collections import Counter, deque

__all__ = ["Writer", "global_writer", "set_global_writer"]

from itertools import cycle

from warg import Number


class Writer(metaclass=ABCMeta):
    """

"""

    def __init__(self, *, interval: int = 1, filters=None, **kwargs):
        self._counter = Counter()
        self._blip_values = iter(cycle([-2.0, 1.0, -1.0, 2.0, 0.0]))
        # self._blip_values = iter(cycle([-1.0,1.0]))
        self._interval = interval
        self.filters = filters

    def filter(self, tag: str) -> bool:
        """

:param tag:
:type tag:
:return:
:rtype:
"""
        is_in_filters = self.filters is None or tag in self.filters
        at_interval = self._counter[tag] % (self._interval + 1) == 0
        return is_in_filters and at_interval

    def __enter__(self):
        global GLOBAL_WRITER_STACK, GLOBAL_WRITER
        GLOBAL_WRITER_STACK.appendleft(self)
        GLOBAL_WRITER = self
        return self._open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        global GLOBAL_WRITER, GLOBAL_WRITER_STACK

        if len(GLOBAL_WRITER_STACK) > 0:
            GLOBAL_WRITER_STACK.popleft()  # pop self

        if len(GLOBAL_WRITER_STACK) > 0:
            GLOBAL_WRITER = GLOBAL_WRITER_STACK.popleft()  # then previous
        else:
            GLOBAL_WRITER = None
        self._close(exc_type, exc_val, exc_tb)

    def scalar(self, tag: str, value: Number, step_i: int = None) -> None:
        """

:param tag:
:type tag:
:param value:
:type value:
:param step_i:
:type step_i:
"""
        if step_i:
            if self.filter(tag):
                self._scalar(tag, value, self._counter[tag])
            self._counter[tag] = step_i
        else:
            if self.filter(tag):
                self._scalar(tag, value, self._counter[tag])
            self._counter[tag] += 1

    def blip(self, tag: str, step_i: int = None) -> None:
        """

:param tag:
:type tag:
:param step_i:
:type step_i:
"""
        if step_i:
            self.scalar(tag, next(self._blip_values), step_i)
        else:
            self.scalar(tag, next(self._blip_values))

    def close(self):
        """

"""
        self._close()

    def open(self):
        """

"""
        self._open()

    @abstractmethod
    def _scalar(self, tag: str, value: float, step: int):
        raise NotImplementedError

    @abstractmethod
    def _close(self, exc_type=None, exc_val=None, exc_tb=None):
        raise NotImplementedError

    @abstractmethod
    def _open(self):
        return self


GLOBAL_WRITER_STACK = deque()
GLOBAL_WRITER = None  #: Writer = None


def global_writer() -> Writer:
    """

:return:
:rtype:
"""
    global GLOBAL_WRITER
    return GLOBAL_WRITER


def set_global_writer(writer: Writer) -> None:
    """

:return:
:rtype:
"""
    global GLOBAL_WRITER
    # if GLOBAL_WRITER:
    # GLOBAL_WRITER_STACK TODO: push to stack if existing?

    GLOBAL_WRITER = writer
