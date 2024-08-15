#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from enum import Enum


class TaskActionTypeEnum(Enum):
    """description"""

    TASK_ACTION_EXEC = 0
    TASK_ACTION_COM_HANDLER = 5
    TASK_ACTION_SEND_MAIL = 6
    TASK_ACTION_SHOW_MESSAGE = 7
