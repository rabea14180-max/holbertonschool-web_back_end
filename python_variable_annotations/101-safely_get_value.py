#!/usr/bin/env python3

"""11. More involved type annotations"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None,
) -> Union[Any, T]:
    """return value for key in dct if present, else default"""
    if key in dct:
        return dct[key]
    return default
