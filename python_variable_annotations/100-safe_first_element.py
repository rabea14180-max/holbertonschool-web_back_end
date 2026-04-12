#!/usr/bin/env python3

"""10. Duck typing - First element of a sequence"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """return first element of lst if not empty, else None"""
    return lst[0] if lst else None
