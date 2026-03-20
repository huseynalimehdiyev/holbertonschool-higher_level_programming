#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list.copy()
    for i in my_list:
        if i % 2 == 0:
            newlist += [True]
        else:
            newlist += [False]
    return newlist