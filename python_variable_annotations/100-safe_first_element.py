#!/usr/bin/env python3
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    return lst[0] if lst else None
