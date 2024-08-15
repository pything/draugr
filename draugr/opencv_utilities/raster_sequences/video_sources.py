#!/usr/bin/env python3

__author__ = "heider"
__doc__ = r"""

           Created on 11/30/22
           """

__all__ = ["get_video_sources"]


from pathlib import Path
from typing import Set

from warg import is_windows


def get_video_sources() -> Set[int]:
    """
    video_source_indices

    :return:
    :rtype:
    """
    if is_windows():
        from os_utilities.windows_utilities.usb_devices import get_windows_usb_devices

        usb_devices = get_windows_usb_devices()
        return {i for i, _ in enumerate(usb_devices)}

    char_devices = [f for f in Path("/dev").iterdir() if f.is_char_device()]
    return set(
        sorted(
            [int(dev.name[-1]) for dev in char_devices if dev.name.startswith("video")]
        )
    )


if __name__ == "__main__":
    print(get_video_sources())

    def iujhasd():
        from opencv_utilities import AsyncVideoStream

        for c in get_video_sources():
            for a in AsyncVideoStream(c):
                print(a)
                break

    iujhasd()
