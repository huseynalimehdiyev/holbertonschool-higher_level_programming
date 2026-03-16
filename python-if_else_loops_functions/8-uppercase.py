#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(str) >= 65 and ord(str) <= 90:
            print("{}".format(i), end="")
        else:
            print("{}".format(chr(ord(i)+26)), end="")
