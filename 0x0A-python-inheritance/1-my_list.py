#!/usr/bin/python3
""" MyList """
class MyList(list):
    """ class that inherits from list """
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
