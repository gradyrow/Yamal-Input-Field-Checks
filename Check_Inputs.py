import re
import os


def input_field_checks(input):

    def hostInput(input):
        pattern = re.compile('^[a-zA-Z0-9 ]+$')
        pattern2 = re.compile('^\d{3}\.\d{3}\.\d{3}\.\d{3}$')
        if pattern.match(input):
            print("Valid input.")
        elif pattern2.match(input):
            print("Valid input.")
        else:
            print("Invalid input. Please enter a number.")

    hostInput(input)


input_field_checks("local host")
input_field_checks("129.132.147.129")
