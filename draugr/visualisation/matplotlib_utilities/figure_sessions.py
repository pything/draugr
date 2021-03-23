#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Christian Heider Nielsen"
__doc__ = r"""

           Created on 15/06/2020
           """

from pathlib import Path
from typing import Iterable, Sequence, Tuple, Union

from matplotlib import pyplot
from warg import AlsoDecorator, passes_kws_to

__all__ = [
    "FigureSession",
    "SubplotSession",
    "MonoChromeStyleSession",
    "NoOutlineSession",
    "OutlineSession",
]

from draugr.visualisation.matplotlib_utilities.matplotlib_utilities import (
    simple_hatch_cycler,
    monochrome_line_cycler,
)
from draugr.visualisation.matplotlib_utilities.quirks import (
    auto_post_hatch,
    fix_edge_gridlines,
)


class FigureSession(AlsoDecorator):
    """
"""

    @passes_kws_to(pyplot.figure)
    def __init__(self, **kws):
        self.fig = pyplot.figure(**kws)

    def __enter__(self) -> pyplot.Figure:
        return self.fig

    def __exit__(self, exc_type, exc_val, exc_tb):
        pyplot.cla()
        pyplot.close(self.fig)
        pyplot.clf()


class SubplotSession(AlsoDecorator):
    """
"""

    @passes_kws_to(pyplot.subplots)
    def __init__(self, return_self: bool = False, **kws):
        self.fig, axs = pyplot.subplots(**kws)
        if not isinstance(axs, Iterable):
            axs = (axs,)
        self.axs = axs
        self.return_self = return_self

    def __enter__(
        self,
    ) -> Union["SubplotSession", Tuple[pyplot.Figure, Sequence[pyplot.Axes]]]:
        if self.return_self:
            return self
        return self.fig, self.axs

    def __exit__(self, exc_type, exc_val, exc_tb):
        # pyplot.cla()
        # pyplot.clf()
        self.fig.clear()
        pyplot.close(self.fig)


class MonoChromeStyleSession(AlsoDecorator):
    """
"""

    def __init__(self, prop_cycler=monochrome_line_cycler):
        self.ctx = pyplot.style.context(
            Path(__file__).parent / "styles" / "monochrome.mplstyle"
        )
        self.prop_cycler = prop_cycler

    def __enter__(self) -> pyplot.Figure:
        a = self.ctx.__enter__()
        pyplot.rcParams.update({"axes.prop_cycle": self.prop_cycler})
        return a

    def __exit__(self, exc_type, exc_val, exc_tb):
        fix_edge_gridlines(pyplot.gca())
        pyplot.tight_layout()
        # auto_post_hatch(pyplot.gca(),hatch_cycler)
        self.ctx.__exit__(exc_type, exc_val, exc_tb)


class NoOutlineSession(AlsoDecorator):
    def __init__(self):
        self._rcParams_copy = pyplot.rcParams.copy()

    def __enter__(self) -> bool:
        pyplot.rcParams.update(
            {
                "patch.edgecolor": "none",
                "patch.force_edgecolor": False,
                "patch.linewidth": 0,
            }
        )
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        pyplot.rcParams = self._rcParams_copy


class OutlineSession(AlsoDecorator):
    def __init__(self):
        self._rcParams_copy = pyplot.rcParams.copy()

    def __enter__(self) -> bool:
        pyplot.rcParams.update(
            {
                "patch.edgecolor": "k",
                "patch.force_edgecolor": True,
                "patch.linewidth": 1.0,
            }
        )
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        pyplot.rcParams = self._rcParams_copy


if __name__ == "__main__":

    def deiajsd():
        """
"""
        for a in range(100):
            with SubplotSession() as a:
                fig, (ax1,) = a
                ax1.set_ylabel("test")

    def asiuhdsada():

        with MonoChromeStyleSession():
            fig, ax = pyplot.subplots(1, 1)
            for x in range(3):
                import numpy

                ax.plot(numpy.random.rand(10), label=f"{x}")

        from matplotlib.pyplot import legend

        legend()
        pyplot.show()

    def no_border_boxplot():
        with NoOutlineSession():
            import numpy

            num = 5
            pyplot.bar(range(num), numpy.random.rand(num))
        pyplot.show()

    def border_boxplot():
        with OutlineSession():
            import numpy

            num = 5
            pyplot.bar(range(num), numpy.random.rand(num))
            pyplot.show()

    # deiajsd()
    no_border_boxplot()
    # border_boxplot()
