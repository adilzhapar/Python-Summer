import socket

SERVER_ADDRESS = ('', 15254)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(1)
print("Ждем подключения клиента...")
while True:
    c, a = server.accept()
    data = c.recv(4096)
    print("Получили от клиента:", data)
    if data == 'stop':
        break
    else:
        int(data) * 10
    c.send(data)
    c.close()