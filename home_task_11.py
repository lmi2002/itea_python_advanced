import socket

sock = socket.socket()
sock.bind(('', 9000))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

sock_client = socket.socket()
sock_client.connect('', 9000)
sock_client.send('hello, world!')
data_client = sock.recv(1024)

print(data)
