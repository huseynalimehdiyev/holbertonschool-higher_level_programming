#!/usr/bin/python3
a = list(input("daxilet").split(" "))
if len(a) == 1:
        print(f"1 argument:")
else:
        print(f"{len(a)} arguments:")
for i in range(0,len(a)):
        print(f"{i+1}: {a[i]}")