import socket

SERVER_ADDRESS = ('localhost', 15254)

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes('stop', encoding='UTF-8'))

data = client.recv(4096)
print(data)