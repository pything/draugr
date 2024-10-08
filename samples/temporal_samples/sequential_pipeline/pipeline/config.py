#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """


TASK_QUEUE_1_NAME = "temporal-community-task-queue"

SCHEDULE_1_NAME = "top-stories-every-10-hours"
WORKFLOW_1_NAME = "temporal-community-workflow"

HOST = "127.0.0.1:7233"  # Go Echo UI @ 8233
NAMESPACE = (
    "default"  # use 'default' for now, must first create a 'mi_integration' namespace
)
