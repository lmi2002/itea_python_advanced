import re


def validate_name(name):
    reg = re.compile('^[a-zA-Z_]+[a-zA-Z_0-9]*$')
    if not reg.match(name):
        raise NameError('Wrong variable name')
    else:
        return True


def input_arg():
    while True:
        arg = input('input name arg: ')
        try:
            if validate_name(arg):
                return arg
        except NameError:
            print('Wrong variable name')


def input_value(arg):
    def enclose(arg):
        while True:
            val = input('input value ' + arg + ' = ')
            try:
                if validate_name(val):
                    return val
            except NameError:
                print('Wrong variable name')
    return enclose


lst = [];
arg = None
value = None
dct = {}
cls = input('Input new class: ')

while True:
    arg = input_arg()
    enclose = input_value(arg)
    val = enclose(arg)
    lst.append({arg:val})
    empty_string = input('Input empty string to quick: ')
    if empty_string == '""' or empty_string == "''":
        break

print(lst)

