#!/usr/bin/python3
" a string to a text file"


def write_file(filename="", text=""):
    "Write smth"
    with open(filename, 'r', encoding='utf-8') as f:
        return f.write(text)

