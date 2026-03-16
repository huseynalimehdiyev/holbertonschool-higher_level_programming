#!/usr/bin/python3
for i in range(1,27):
    if i % 2 == 0:
      print(chr(65+26-i), end="")
    else:
       print(chr(97+26-i), end="")
