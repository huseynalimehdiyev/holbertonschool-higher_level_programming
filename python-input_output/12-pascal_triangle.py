#!/usr/bin/python3
"""Interview question"""


def pascal_triangle(n):
    """Find Pascal triangle"""
    
    if n <= 0:
        return []
    else:
        triangle = []
        for i in range(n):
