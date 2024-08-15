#!/usr/bin/env python3

__author__ = "heider"
__doc__ = r"""

           Created on 8/24/22
           """

__all__ = [
    "in_ipynb",
    "in_docker",
    "can_ping_subprocess",
    "can_ping",
    "hostname_resolves",
]

import os
import subprocess
import sys
from pathlib import Path

from warg.functions import text_in_file
from warg.os_utilities import is_windows


def in_ipynb(verbose: bool = False) -> bool:
    """

    :return:
    :rtype:
    """
    try:
        from IPython import get_ipython
        import jupyter

        shell = get_ipython().__class__.__name__
        if verbose:
            print(f"found shell: {shell}")
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        if verbose:
            print(f"Probably standard Python interpreter")
        return False  # Probably standard Python interpreter
    except ModuleNotFoundError:
        if "ipykernel" in sys.modules:
            if verbose:
                print(f"Found ipykernel in sys.modules")
            return True

        if verbose:
            print(f"Did not find Ipython")
        return False  # Did not find Ipython


def in_docker(
    # hostname: str = "host.docker.internal"
) -> bool:
    """ """
    return (
        Path("/.dockerenv").exists()  # short circuits
        or text_in_file("docker", Path("/proc/self/cgroup"))  # short circuits
        # or (hostname_resolves(hostname) and can_ping_subprocess(hostname))
    )


def can_ping(hostname: str) -> bool:
    return not bool(os.system(f"ping -{'n' if is_windows() else 'c'} 1 {hostname}"))


def hostname_resolves(hostname: str) -> bool:
    try:
        import socket

        socket.gethostbyname(hostname)
        return True
    except OSError:
        return False


def can_ping_subprocess(hostname: str) -> bool:
    try:
        return not bool(
            subprocess.check_output(
                f"ping -{'n' if is_windows() else 'c'} 1 {hostname}",
                shell=True,
            )
        )
    except Exception:
        return False


if __name__ == "__main__":
    print(in_ipynb())
    print(in_docker())
    # print(hostname_resolves("host.docker.internal"))
    print(can_ping_subprocess("host.docker.internal"))
    print(can_ping("host.docker.internal"))
    # print(hostname_resolves())
