#!/usr/bin/python3

from utils import access_nested_map

nested_map = {"a": 1}
item = access_nested_map(nested_map, ("a", "b"))
print(item)