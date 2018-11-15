#!/usr/bin/env python
# -*- coding: utf-8 -*

import socket
import os

def run():
    sock = socket.socket()
    sock.bind(('', 9000))
    sock.listen(5)
    conn, addr = sock.accept()
    print('connection: ' + addr)
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            break
        conn.send(data.upper())

    conn.close()


if __name__ == '__main__':
    run()
