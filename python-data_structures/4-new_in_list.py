#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or len(my_list) <= idx:
        return new_list
    else:
        return new_list[idx] == element
