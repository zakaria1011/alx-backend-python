#!/usr/bin/python3
from functools import wraps
from typing import Callable

def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method."""
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)

class Calculator:
    def __init__(self):
        self._history = []

    @memoize
    def add(self, x, y):
        """Add two numbers."""
        result = x + y
        self._history.append(f"Added {x} and {y}, result is {result}")
        return result

# Create an instance of the Calculator class
calculator = Calculator()

# Perform some addition operations
print(calculator.add(2, 3))  # Outputs: 5
print(calculator.add(2, 3))  # Outputs: 5 (retrieved from cache)

# Print the history of operations
print(calculator._history)
