#!/usr/bin/python3
for num in range(99):
    if num < 10:
        num = '0' + str(num)
    print("{}".format(num), end = ", ")
print(num+1)
