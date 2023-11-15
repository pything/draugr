# -*- coding: utf-8 -*-
from itertools import cycle

doors = 100 * [False]
for ith_pass in range(100):
    doors = [
        not d if s else d
        for s, d in zip(
            cycle([True] if ith_pass % 5 == 0 else [False] * ith_pass + [True]), doors
        )
    ]
print(f"Generator: {doors}")
