#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_b) < 2:
        return tuple_a[:2]
    elif len(tuple_a) > 2 and len(tuple_b) > 2:
            return tuple_a[:2]+tuple_b[:2]
    else:
        return tuple_a + tuple_b
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)
