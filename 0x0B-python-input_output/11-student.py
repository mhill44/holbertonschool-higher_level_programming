#!/usr/bin/python3
""" Student Class """


class Student:
    """ This is a class named Student """

    def __init__(self, first_name, last_name, age):
        """ Initialize the Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON
        """
        if type(attrs) is not list:
            return self.__dict__
        for i in attrs:
            if type(i) is not str:
                return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """ This replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
