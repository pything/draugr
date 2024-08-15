#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"

__doc__ = r"""
"""
from enum import Enum

__all__ = ["HttpMethodEnum"]


class HttpMethodEnum(Enum):
    get = "GET"
    post = "POST"
    head = "HEAD"
    put = "PUT"
    delete = "DELETE"
    connect = "CONNECT"
    options = "OPTIONS"
    trace = "TRACE"
    patch = "PATCH"
