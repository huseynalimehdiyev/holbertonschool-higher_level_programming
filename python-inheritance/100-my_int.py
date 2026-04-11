#!/usr/bin/python3
"""MyInt class that inverts == and !="""

class MyInt(int):
    """Rebel integer class"""

    def __eq__(self, other):
        """Invert == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != operator"""
        return super().__eq__(other)
