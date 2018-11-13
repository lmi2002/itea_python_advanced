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


def output(self):
    describe = 'Class <{}>:\n'.format(self.__class__.__name__)
    params = '\n'.join(['{key} = {value}'.format(key=k, value=v) for k, v in self.__class__.__dict__.items() if
                        not k.startswith('__')])
    return describe + params


def main():
    arg = None
    value = None
    dct = {}
    cls = input('Input new class: ')

    while True:
        arg = input_arg()
        enclose = input_value(arg)
        val = enclose(arg)
        dct.update({arg: val})
        empty_string = input('Input empty string to quick: ')
        if empty_string == '""' or empty_string == "''":
            break

    dct.update({'__str__': output})
    Myclass = type(cls, (), dct)
    a = Myclass()
    print(a)
