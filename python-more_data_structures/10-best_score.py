#!/usr/bin/python3
def best_score(a_dictionary):
    max_val = 0
    for i in a_dictionary.keys():
        if a_dictionary[i] > max_val:
            max_val == a_dictionary[i]
    return a_dictionary[max_val]
