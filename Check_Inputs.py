import re
import os


def bad_input_exception(input, pattern, invalid_message):
    if pattern.match(input) is None:
        print(invalid_message)  # bad __ input, create exception


def hostInput(input):
    host = re.compile('^[a-zA-Z0-9 ]+$|^\d{3}\.\d{3}\.\d{3}\.\d{3}$')
    bad_input_exception(input, host, "Bad host")

hostInput("129.132.147.128")


def stateInput(input):
    state = re.compile(r'\b(present|absent)\b', re.IGNORECASE)
    bad_input_exception(input, state, "Bad state input")


stateInput("present")


def nameInput(input):
    name = re.compile('^[a-zA-Z0-9 ,.?!@#$%^&*();:/_+=-]+$')
    bad_input_exception(input, name, "Bad name input")


nameInput("Home Host Server")


def portInput(input):
    port = re.compile('^[0-9]{1,5}$')
    bad_input_exception(input, port, "Bad state input")

portInput("2556")

def emailInput(input):
    email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    bad_input_exception(input, email, "Bad state input")


emailInput("gradyrow@hotmail.com")


def bodyMsgInput(input):
    bodyMsg = re.compile('^"[a-zA-Z0-9 ,.?!@#$%^&*();:/_+=-]+"$')
    bad_input_exception(input, bodyMsg, "Bad body/msg input")


bodyMsgInput('"This is and email notification"')



def repoInput(input):
    repo = re.compile(r'^https://github\.com/[^/]+/[^/]+\.git$')
    bad_input_exception(input, repo, "Bad repo input")


repoInput('https://github.com/example/repo.git')


def destInput(input):
    dest = re.compile(r'^/[^/]+(/[^/]*)*$')
    bad_input_exception(input, dest, "Bad state input")


destInput('/path/to/the/destination')

