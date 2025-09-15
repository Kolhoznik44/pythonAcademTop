import socket

ipServer = "127.0.0.1"
port = 48084
sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockClient.connect((ipServer, port))
sockClient.send("Hello World".encode())
data = sockClient.recv(1024)
print(f"Ответ: {data.decode()}")