#!/usr/bin/env python
# -*- coding: utf-8 -*

import socket

sock = socket.socket()
sock.connect(('localhost', 9000))
i = input('Введите данные:')
b_string = i.encode()
sock.send(b_string)

data = sock.recv(1024)
sock.close()

print(data)
