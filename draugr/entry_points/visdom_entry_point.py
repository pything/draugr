#!/usr/bin/env python3
__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""
"""
__all__ = []


# http://localhost:8097
# python -m visdom.server


def main():
    """
    Will start a visdom server
    """
    import visdom.server as server

    server.main()


if __name__ == "__main__":
    main()
