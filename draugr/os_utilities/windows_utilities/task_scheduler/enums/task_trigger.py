#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from enum import Enum


class TaskTriggerEnum(Enum):
    """description"""

    TASK_TRIGGER_EVENT = 0
    TASK_TRIGGER_TIME = 1
    TASK_TRIGGER_DAILY = 2
    TASK_TRIGGER_WEEKLY = 3
    TASK_TRIGGER_MONTHLY = 4
    TASK_TRIGGER_MONTHLYDOW = 5
    TASK_TRIGGER_IDLE = 6
    TASK_TRIGGER_REGISTRATION = 7
    TASK_TRIGGER_BOOT = 8
    TASK_TRIGGER_LOGON = 9
    TASK_TRIGGER_SESSION_STATE_CHANGE = 11
