#!/usr/bin/python3
""" My list class """


class MyList(list):
    """ My list class """
    def __init__(self):
        """ Init the method """
        super().__init__()

    def print_sorted(self):
        """ This prints the list in ascending order """
        print(sorted(self))
