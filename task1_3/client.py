import socket
from datetime import datetime as dt


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ('127.0.0.1', 3001)
)

while True:
    data = client.recv(2048)
    print(data.decode('utf-8'))

    while True:
        client_input = input('---> ')
        client.send(client_input.encode('utf-8'))

        if client_input == 'close':
            data = client.recv(2048)
            print(f"[{str(dt.now())}]", data.decode("utf-8"))
