#!/usr/bin/env python3

"""12. Type checking"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """repeat each element of lst factor times, in order"""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
