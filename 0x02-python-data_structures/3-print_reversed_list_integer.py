#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None:
        my_list = []
    if not my_list:
        return None
    else:
        my_list.reverse()
    for i in my_list:
        print("{:d}".format(my_list[i]))