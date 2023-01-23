#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lists = []
    for num in my_list:
        new_lists.append(True) if num % 2 == 0 else new_lists.append(False)
    return new_lists
