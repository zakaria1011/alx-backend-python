#!/usr/bin/env python3
""" function returning a function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returning a function"""
    def multiplier_fct(x: float) -> float:
        """ return x*multiplier"""
        return x * multiplier
    return multiplier_fct
