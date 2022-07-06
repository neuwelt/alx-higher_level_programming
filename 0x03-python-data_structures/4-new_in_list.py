#!/usr/bin/python3
def new_list_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new = [x for x in my_list]
        new[idx] = element
        return new
