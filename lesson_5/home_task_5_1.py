import sys
import re


def input_value(key):
    def enclose(key):
        while True:
            return input('input value ' + key + ' = ')
    return enclose


key = None
value = None
dct = {}
cls = input('Input new class: ')

while True:
    key = input('input name arg - ')
    enclose = input_value(key)
    enclose(key)
    empty_string = input('Want to finish typing? Yes: input an empty string, Not: press enter!')


def decorator_validate_name(func):
    def wrapper(func):
        name = func()
        reg = re.compile('^[a-zA-Z_]+[a-zA-Z_0-9]*$')
        if not reg.match(name):
            raise NameError('Wrong variable name')
    return wrapper



def validate_name(name):
    reg = re.compile('^[a-zA-Z_]+[a-zA-Z_0-9]*$')
    if not reg.match(name):
        raise NameError('Wrong variable name')

