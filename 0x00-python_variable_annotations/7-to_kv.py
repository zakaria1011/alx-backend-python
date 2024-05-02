#!/usr/bin/env python3
""" function the return tuple """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple"""
    return k, v**2
