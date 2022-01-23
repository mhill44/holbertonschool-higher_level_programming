#!/usr/bin/python3
"""My_List class:
Creates a class MyList that inherits from the list class.
"""

"""Class MyList inherits from list."""


class MyList(list):
    def print_sorted(self):
        newList = sorted(self[:])
        print("{}".format(newList))
