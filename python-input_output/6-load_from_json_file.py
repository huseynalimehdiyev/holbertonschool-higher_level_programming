#!/usr/bin/python3
"""JSON"""

import json


def load_from_json_file(filename):
    """Function"""
    with open(filename, 'w', encoding="utf-8") as f:
        return json.load()
