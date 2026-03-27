#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
    except NameError:
        print("Error for name")
    else:
        print("Unknown error")
