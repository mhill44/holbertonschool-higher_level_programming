#!/usr/bin/python3
""" A Student Class """


class Student:
    """ A class called Student """

    def __init__(self, first_name, last_name, age):
        """ This Initializes the Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This retrieves a dictionary representation of a Student instance """
        return self.__dict__
