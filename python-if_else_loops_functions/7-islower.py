#!/usr/bin/python3
def islower(c):
    c = chr(c)
    if ord(c) >= 97 or ord(c) <= 123:
        return True
    else:
        return False