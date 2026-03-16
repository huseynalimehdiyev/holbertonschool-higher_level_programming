#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            print("{}".format(i), end="")
        else:
            print("{}".format(chr(ord(i)+32)), end="")
