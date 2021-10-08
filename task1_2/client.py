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
    client.send(input('---> ').encode('utf-8'))

    data = client.recv(2048)
    print(f"[{str(dt.now())}]", data.decode("utf-8"))
