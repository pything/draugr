#!/usr/bin/env python3

__author__ = "Christian Heider Lindbjerg"
__doc__ = r"""

           Created on 15/06/2020
           """

from pathlib import Path
from typing import Iterable, Optional, Sequence, Tuple, Union

from cycler import Cycler
from matplotlib import pyplot

from warg import AlsoDecorator, passes_kws_to

__all__ = [
    "FigureSession",
    "SubplotSession",
    "MonoChromeStyleSession",
    "NoOutlineSession",
    "OutlineSession",
    "StyleSession",
]

from draugr.visualisation.matplotlib_utilities.matplotlib_utilities import (
    monochrome_line_cycler,
)
from draugr.visualisation.matplotlib_utilities.quirks import fix_edge_gridlines
from draugr.visualisation.matplotlib_utilities.styles.cyclers import (
    color_cycler,
    line_cycler,
)
import subprocess
from typing import MutableMapping


class FigureSession(AlsoDecorator):
    """
    maintains a figure session while in context

    """

    @passes_kws_to(pyplot.figure)
    def __init__(self, **kwargs: MutableMapping):
        self.fig = pyplot.figure(**kwargs)

    def __enter__(self) -> pyplot.Figure:
        return self.fig

    def __exit__(self, exc_type, exc_val, exc_tb):
        pyplot.cla()
        pyplot.close(self.fig)
        pyplot.clf()


class SubplotSession(AlsoDecorator):
    """
    maintains a subplot session while in context

    """

    @passes_kws_to(pyplot.subplots)
    def __init__(self, return_self: bool = False, **kwargs: MutableMapping):
        self.fig, axs = pyplot.subplots(**kwargs)
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


class StyleSession(AlsoDecorator):
    """
    maintains a style session while in context
    """

    def __init__(
        self,
        style_path: Path = Path(__file__).parent / "styles" / "publish_color.mplstyle",
        prop_cycler: Optional[Cycler] = line_cycler + color_cycler,
        latex_path: Path = Path(
            r"C:\Users\deter\AppData\Local\Programs\MiKTeX\miktex\bin\x64\latex.exe"
        ),
        # Path('latex')
    ):
        """
        Set styling for context

        :param style_path: path to style file
        :param prop_cycler: overwrite prop_cycler with a programmatically defined one
        """
        self.ctx = pyplot.style.context(style_path)
        self.prop_cycler = prop_cycler
        self.latex_path = latex_path

    def __enter__(self) -> pyplot.Figure:
        a = self.ctx.__enter__()
        if pyplot.rcParams["text.usetex"]:
            try:
                version_command = "--version"  # -v
                report = subprocess.check_output(
                    f"{self.latex_path} {version_command}", stderr=subprocess.STDOUT
                )
            except FileNotFoundError as exc:
                msg = f'No tex: {"latex"}'
                # raise RuntimeError(msg)
                print(f"{msg}, disabling")
                pyplot.rcParams.update({"text.usetex": False})
        if self.prop_cycler:
            pyplot.rcParams.update({"axes.prop_cycle": self.prop_cycler})
        return a

    def __exit__(self, exc_type, exc_val, exc_tb):
        fix_edge_gridlines(pyplot.gca())
        # pyplot.tight_layout()
        # auto_post_hatch(pyplot.gca(),hatch_cycler)
        self.ctx.__exit__(exc_type, exc_val, exc_tb)


class MonoChromeStyleSession(StyleSession):
    """
    maintains a style session with monochrome style while in context

    """

    def __init__(
        self,
        style_path=Path(__file__).parent / "styles" / "monochrome.mplstyle",
        prop_cycler: Optional[Cycler] = monochrome_line_cycler,
    ):
        """

        :param style_path:
        :param prop_cycler:
        """
        super().__init__(style_path, prop_cycler)


class NoOutlineSession(AlsoDecorator):
    """maintains a style session with no outline while in context"""

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
    """maintains a style session with outlines while in context"""

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

    def deiajsd() -> None:
        """
        :rtype: None
        """
        for _ in range(100):
            with SubplotSession() as a:
                fig, (ax1,) = a
                ax1.set_ylabel("test")

    def asiuhdsada() -> None:
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

    def no_border_boxplot() -> None:
        """
        :rtype: None
        """
        with NoOutlineSession():
            import numpy

            num = 5
            pyplot.bar(range(num), numpy.random.rand(num))
        pyplot.show()

    def border_boxplot() -> None:
        """
        :rtype: None
        """
        with OutlineSession():
            import numpy

            num = 5
            pyplot.bar(range(num), numpy.random.rand(num))
            pyplot.show()

    # deiajsd()
    no_border_boxplot()
    # border_boxplot()
