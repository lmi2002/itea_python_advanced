import json
import pickle


def exporter():
    f = open(r'C:\Users\Star\PycharmProjects\itea_python_advanced\file.txt', 'rb')
    line = json.loads()
    f.close()
    print(line)


def greeting(greet):
    def enclosure(name):
        return greet + name
    return enclosure


p = greeting('Hello ')
print(p)
print(p('Sergey'))
print(p('Vitaliy'))
