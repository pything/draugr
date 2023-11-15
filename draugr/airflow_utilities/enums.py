# -*- coding: utf-8 -*-
from enum import Enum
from sorcery import assigned_names


__all__ = ["AutoRemoveEnum"]


class AutoRemoveEnum(Enum):
    never, success, force = assigned_names()
