#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    for i in range(1,len(my_list)):
        if my_list[i] > max_value:
            max_value == i
    print("Max: {:d}".format(max_value))
