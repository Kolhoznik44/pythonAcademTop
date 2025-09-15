#-======- Код клиента - запустить в отдельном окне и проекте -=======-

import socket

ipServer = "127.0.0.1"
port = 48084
sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockClient.connect((ipServer, port))

while True:
    message = input()
    if message == "quit":
        sockClient.close()
        break
    sockClient.send(message.encode())
    data = ""
    # while True:
    dataBinary = sockClient.recv(1024)
    data += dataBinary.decode()
    print(f"Ответ: {data}")
