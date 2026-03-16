#!/usr/bin/python3
for num in range(98):
    if num < 10:
        print("0{}".format(num), end = ",")
    else:
       print("{}".format(num), end = ",") 