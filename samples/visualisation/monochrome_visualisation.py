#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

            on ubuntu ensure to run:
             sudo apt install dvipng texlive-latex-extra texlive-fonts-recommended


           Created on 24-02-2021
           """

import numpy
from draugr.visualisation import (
    MonoChromeStyleSession,
    auto_post_hatch,
    monochrome_hatch_cycler,
    simple_hatch_cycler,
    use_monochrome_style,
)
from matplotlib import pyplot
from matplotlib.pyplot import legend


def line_plot() -> None:
    """
    :rtype: None
    """
    with MonoChromeStyleSession():
        fig, ax = pyplot.subplots(1, 1)
        for x in range(3):
            import numpy

            ax.plot(numpy.random.rand(10), label=f"{x}")

    from matplotlib.pyplot import legend

    legend()
    pyplot.show()


def bar_plot() -> None:
    """
    :rtype: None
    """
    use_monochrome_style(prop_cycler=monochrome_hatch_cycler)

    fig, ax = pyplot.subplots(1, 1)

    for x in range(3):
        ax.bar(x, numpy.random.randint(2, 10), label=f"{x}")

    legend()
    from draugr.visualisation.matplotlib_utilities.quirks import fix_edge_gridlines

    fix_edge_gridlines(ax)
    auto_post_hatch(ax, simple_hatch_cycler)
    pyplot.show()


if __name__ == "__main__":
    line_plot()
    bar_plot()
