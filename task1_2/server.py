import socket
from datetime import datetime as dt
import time

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind(
    ('127.0.0.1', 3001)
)

server.listen(5)
print('Server is listening')

while True:
    user_socket, address = server.accept()
    user_socket.send('You are connected'.encode('utf-8'))
    print(f'[{str(dt.now())}] User {user_socket} connected!')

    data = user_socket.recv(2048)
    print(f'[{str(dt.now())}] {address[0]} ---> ', data.decode('utf-8'))

    time.sleep(5)
    user_socket.send('Data sent successfully(close connection)'.encode('utf-8'))
    user_socket.close()
