#!/usr/bin/env python3
import pytest

from warg import ensure_in_sys_path, find_nearest_ancestral_relative

ensure_in_sys_path(find_nearest_ancestral_relative("draugr").parent)
from draugr.drawers import discrete_scroll_plot

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 9/2/19
           """


@pytest.mark.skip
def test_series_scroll_plot():
    gen = iter(
        [
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ]
    )
    discrete_scroll_plot(gen, labels=("a", "b", "c"))
    assert True


if __name__ == "__main__":
    test_series_scroll_plot()
