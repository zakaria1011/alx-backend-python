#!/usr/bin/env python3
""" annotate a function """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list of tuple of sequence and int """
    return [(i, len(i)) for i in lst]
