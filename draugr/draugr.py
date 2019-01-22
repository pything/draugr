#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .draugr_utilties import (COLORS, PrintStyle, generate_style, get_terminal_size, scale)

__author__ = 'cnheider'

from typing import Sized

import numpy as np


# sys.stdout.write(generate_style(u'Draugr Ûnicöde Probe\n', underline=True, italic=True))


def terminal_plot(y: Sized,
                  *,
                  x=None,
                  title='',
                  rows=None,
                  columns=None,
                  percent_size=(.80, .80),
                  x_offsets=(1, 1),
                  y_offsets=(1, 1),
                  printer=print,
                  print_summary=True,
                  plot_character=u'\u2981',
                  print_style: PrintStyle = None
                  ):
  '''
  x, y list of values on x- and y-axis
  plot those values within canvas size (rows and columns)
  '''

  num_y = len(y)
  if num_y == 0:
    return

  if x:
    if len(x) != num_y:
      raise ValueError(f'x argument must match the length of y, got x:{len(x)} and y:{num_y}')
  else:
    x = range(num_y)

  actual_columns = columns
  actual_rows = rows
  border_size = (1, 1)

  if not rows or not columns:
    terminal_size = get_terminal_size()
    if percent_size:
      columns, rows = int(terminal_size.columns * percent_size[0]), int(terminal_size.rows * percent_size[1])

    actual_columns = columns - sum(x_offsets) - sum(border_size)
    actual_rows = rows - sum(y_offsets) - sum(border_size)

  # Scale points such that they fit on canvas
  x_scaled = scale(x, actual_columns)
  y_scaled = scale(y, actual_rows)

  # Create empty canvas
  canvas = [[' ' for _ in range(columns)] for _ in range(rows)]

  # Create borders
  for iy in range(1, rows - 1):
    canvas[iy][0] = u'\u2502'
    canvas[iy][columns - 1] = u'\u2502'
  for ix in range(1, columns - 1):
    canvas[0][ix] = u'\u2500'
    canvas[rows - 1][ix] = u'\u2500'
  canvas[0][0] = u'\u250c'
  canvas[0][columns - 1] = u'\u2510'
  canvas[rows - 1][0] = u'\u2514'
  canvas[rows - 1][columns - 1] = u'\u2518'

  # Add scaled points to canvas
  for ix, iy in zip(x_scaled, y_scaled):
    canvas[1 + y_offsets[0] + (actual_rows - iy)][1 + x_offsets[0] + ix] = plot_character

  print('\n')
  # Print rows of canvas
  for row in [''.join(row) for row in canvas]:
    if print_style:
      printer(print_style(row))
    else:
      printer(row)

  # Print scale
  if print_summary:
    summary = f'{title} - (min, max): x({min(x)}, {max(x)}), y({min(y)}, {max(y)})\n'
    if print_style:
      printer(print_style(summary))
    else:
      printer(summary)


def styled_terminal_plot_stats_shared_x(stats, *, styles=None, **kwargs):
  if styles is None:
    styles = [generate_style(color=color, highlight=True) for color, _ in zip(COLORS.keys(),
                                                                              range(len(stats)))]
  return terminal_plot_stats_shared_x(stats, styles=styles, **kwargs)


def terminal_plot_stats_shared_x(stats,
                                 *,
                                 x=None,
                                 styles=None,
                                 printer=print,
                                 margin=.25,
                                 summary=True):
  num_stats = len(stats)

  y_size = (1 - margin) / num_stats

  if styles:
    if len(styles) != num_stats:
      raise ValueError(f'styles argument must match the length of stats, got styles:{len(styles)} and '
                       f'stats:{num_stats}')
  else:
    styles = [None for _ in range(num_stats)]

  for (key, stat), sty in zip(stats.items(), styles):
    terminal_plot(
        stat.running_value,
        title=key,
        x=x,
        printer=printer,
        print_style=sty,
        percent_size=(1, y_size),
        print_summary=summary
        )


if __name__ == '__main__':
  terminal_plot(np.tile(range(9), 4), plot_character='o')
