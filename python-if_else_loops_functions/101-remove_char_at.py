#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str[:]
    if n >= 0:
        return new_str[:n] + new_str[n+1:]
    else:
        return new_str
