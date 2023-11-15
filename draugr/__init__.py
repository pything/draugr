#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__project__ = "Draugr"
__author__ = "Christian Heider Lindbjerg"
__version__ = "1.1.6"
__doc__ = r"""
Created on 27/04/2019

@author: cnheider

"""


try:
    from importlib.resources import files
    from importlib.metadata import PackageNotFoundError
except (ModuleNotFoundError, ImportError) as e:
    from importlib_metadata import PackageNotFoundError
    from importlib_resources import files

from warg import package_is_editable, clean_string, get_version
from apppath import AppPath
from pathlib import Path

# from .drawers import *
# from .writers import *
# from .opencv_utilities import *
# from .torch_utilities import *
# from .stopping import *
# from .numpy_utilities import *
# from .visualisation import *
# from .metrics import *
# from .python_utilities import *

with open(Path(__file__).parent / "README.md", "r") as this_init_file:
    __doc__ += this_init_file.read()

# with open(Path(__file__).parent.parent / "README.md", "r") as this_init_file:
#    __doc__ += this_init_file.read()

__all__ = [
    "PROJECT_APP_PATH",
    "PROJECT_NAME",
    "PROJECT_VERSION",
    "PROJECT_ORGANISATION",
    "PROJECT_AUTHOR",
    "PROJECT_YEAR",
    "INCLUDE_PROJECT_READMES",
    "PACKAGE_DATA_PATH",
]

PROJECT_ORGANISATION = clean_string("Pything")
PROJECT_NAME = clean_string(__project__)
PROJECT_VERSION = __version__
PROJECT_YEAR = 2018
PROJECT_AUTHOR = clean_string(__author__)
PROJECT_APP_PATH = AppPath(app_name=PROJECT_NAME, app_author=PROJECT_AUTHOR)
INCLUDE_PROJECT_READMES = False

__url__ = f"https://github.com/{PROJECT_ORGANISATION.lower()}/{PROJECT_NAME}"

PACKAGE_DATA_PATH = files(PROJECT_NAME) / "data"

try:
    DEVELOP = package_is_editable(PROJECT_NAME)
except PackageNotFoundError as e:
    DEVELOP = True


__version__ = get_version(__version__, append_time=DEVELOP)

__version_info__ = tuple(int(segment) for segment in __version__.split("."))

if __name__ == "__main__":
    print(__version__)
