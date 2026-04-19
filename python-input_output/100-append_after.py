#!/usr/bin/python3
"""Shebang"""


def append_after(filename="", search_string="", new_string=""):
    """Function"""
    updated_content = ""

    with open(filename, "r") as f:
        for line in f:
            updated_content += line
            if search_string in line:
                updated_content += new_string

    with open(filename, "w") as f:
        f.write(updated_content)