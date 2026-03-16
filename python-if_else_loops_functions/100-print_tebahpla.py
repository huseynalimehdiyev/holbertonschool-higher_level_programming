#!/usr/bin/python3
for i in range(1, 27):
    print("{}".format((chr(65 + 26 - i))) if i % 2 == 0\
           else "{}".format((chr(123 - i))), end="")
