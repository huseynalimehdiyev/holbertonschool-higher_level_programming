#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif len(my_list) < idx:
        return None
    else:
        print("element at index {} is {}".format(idx, my_list[idx]))
