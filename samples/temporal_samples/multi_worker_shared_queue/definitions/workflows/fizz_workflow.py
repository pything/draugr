#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from datetime import timedelta

from temporalio import workflow

# Import our activity, passing it through the sandbox
with workflow.unsafe.imports_passed_through():
    from ..activities.fizz_activity import fizz_activity


@workflow.defn
class FizzWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            fizz_activity, name, schedule_to_close_timeout=timedelta(seconds=5)
        )
