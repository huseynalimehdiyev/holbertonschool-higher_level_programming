#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]      
if len(args) == 1:
    print(f"1 argument:")
elif len(args) == 0:
    print(f"0 arguments.")
else:
    print(f"{len(args)} arguments:")
for i in range(0, len(args)):
    print(f"{i+1}: {args[i]}")
