#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 19/03/2020
           """

from typing import Dict, List


def get_windows_usb_devices(
    root_usb_key: str = r"SYSTEM\CurrentControlSet\Enum\USB",
    usb_service_type: str = "usbvideo",  # TODO: ENUMIFY service_type
) -> List[Dict[str, str]]:
    try:
        import winreg
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError((e, "missing winreg"))

    WIN_ERROR_CODE_NO_DATA = 259

    usb_devices = []

    sub_keys = []
    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, root_usb_key) as root_usb:
        index = 0
        while True:
            try:
                subkey = winreg.EnumKey(root_usb, index)
                if subkey.startswith("VID"):
                    sub_keys.append(root_usb_key + "\\" + str(subkey))
                index += 1
            except OSError as e:
                if e.winerror == WIN_ERROR_CODE_NO_DATA:  # No more data is available
                    break
                elif e.winerror == 234:  # more data is available
                    index += 1
                    continue
                raise e

    sub_sub_keys = []
    for sub_key in sub_keys:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            sub_key,
        ) as vid_key:
            index = 0
            while True:
                try:
                    sub_sub_keys.append(sub_key + "\\" + winreg.EnumKey(vid_key, index))
                    index += 1
                except OSError as e:
                    if (
                        e.winerror == WIN_ERROR_CODE_NO_DATA
                    ):  # No more data is available
                        break
                    elif e.winerror == 234:  # more data is available
                        index += 1
                        continue
                    raise e

    for sub_sub_key in sub_sub_keys:
        with winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            sub_sub_key,
        ) as dev_key:  # TODO: USE OpenKeyEx instead for subkeys...
            service_type = winreg.QueryValueEx(dev_key, "Service")[
                0
            ]  # TODO: ENUMIFY __name's
            if service_type == usb_service_type:
                name = winreg.QueryValueEx(dev_key, "FriendlyName")[0]
                desc = winreg.QueryValueEx(dev_key, "DeviceDesc")[0]
                usb_devices.append({name: desc})

    return usb_devices
