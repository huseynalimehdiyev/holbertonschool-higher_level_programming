#!/usr/bin/python3
for i in range(10):
    for k in range(i+1,10):
        num=str(i)+str(k)
        if str(i) == '8' and str(k) == '9':
            print("{}".format(num))
        else:
            print("{}".format(num), end=", ")

