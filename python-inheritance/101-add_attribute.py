#!/usr/bin/python3
"""Function to add attribute if possible"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to obj if possible"""

    if hasattr(obj, "__dict__"):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
