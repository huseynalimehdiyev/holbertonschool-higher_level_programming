#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str[:]
    return new_str[:n] + new_str[n+1:]
print(remove_char_at("BEst School", 3))