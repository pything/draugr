#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 31-10-2020
           """

if __name__ == "__main__":
    from draugr.os_utilities.linux_utilities.gtk_utilities import GtkThemePreferences

    GtkThemePreferences().prefer_dark_mode = False
