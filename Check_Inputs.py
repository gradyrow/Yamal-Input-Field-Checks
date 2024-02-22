import re
import os


def hostInput(input):
    pattern = re.compile('^[a-zA-Z0-9 ]+$')
    pattern2 = re.compile('^\d{3}\.\d{3}\.\d{3}\.\d{3}$')
    if pattern.match(input):
        print("Valid host input.")
    elif pattern2.match(input):
        print("Valid host input.")
    else:
        print("Invalid input. Please enter a number.")


hostInput("129.132.147.128")


def stateInput(input):
    pattern = re.compile(r'\b(present|absent)\b', re.IGNORECASE)
    if pattern.match(input):
        print("Valid state input.")
    else:
        print("Invalid input. Please enter present or absent")


stateInput("present")


def nameInput(input):
    pattern = re.compile('^[a-zA-Z0-9 ]+$')
    if pattern.match(input):
        print("Valid name input.")
    else:
        print("Invalid input.")

nameInput("Home Host Server")


def portInput(input):
    pattern = re.compile('^[0-9]{1,5}$')
    if pattern.match(input):
        print("Valid port input.")
    else:
        print("Invalid port input.")

portInput("2556")

def toFromInput(input):
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if pattern.match(input):
        print("Valid email input.")
    else:
        print("Invalid input.")


toFromInput("gradyrow@hotmail.com")


def bodyMsgInput(input):
    pattern = re.compile('^"[a-zA-Z0-9 ]+"$')
    pattern2 = re.compile('^\d{3}\.\d{3}\.\d{3}\.\d{3}$')
    if pattern.match(input):
        print("Valid bodyMsg input.")
    elif pattern2.match(input):
        print("Valid bodyMsg input.")
    else:
        print("Invalid input.")


bodyMsgInput('"This is and email notification"')



def repoInput(input):
    pattern = re.compile(r'^https://github\.com/[^/]+/[^/]+\.git$')
    if pattern.match(input):
        print("Valid repo input.")
    else:
        print("Invalid repo input.")


repoInput('https://github.com/example/repo.git')


def destInput(input):
    pattern = re.compile(r'^/[^/]+(/[^/]*)*$')
    if pattern.match(input):
        print("Valid dest input.")
    else:
        print("Invalid dest input.")


destInput('/path/to/the/destination')

