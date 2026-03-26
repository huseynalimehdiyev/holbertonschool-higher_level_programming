#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if my_list.count(i) == 1:
            new_list.appemd(i)
    return new_list
