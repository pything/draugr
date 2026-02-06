__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from temporalio import activity


@activity.defn
async def fizz_activity(name: str) -> str:
    return f"fizz, {name}!"
