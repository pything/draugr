#!/usr/bin/env python3

__author__ = "heider"
__doc__ = r"""

           Created on 8/22/22
           """

__all__ = []

import time

import schedule


def job():
    print("I'm working...")


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
