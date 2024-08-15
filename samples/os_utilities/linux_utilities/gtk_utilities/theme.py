#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 31-10-2020
           """

if __name__ == "__main__":
    from draugr.os_utilities.linux_utilities.gtk_utilities import GtkThemePreferences

    print(GtkThemePreferences().theme)
