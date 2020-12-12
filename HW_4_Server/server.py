import socket
import json

HOST = '127.0.0.1'
PORT = 11111

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen()
conn, addr = serverSocket.accept()
data = json.loads(conn.recv(1024))
print(f'Server recive data from client\n {data}')
# Calculating average from received list
data['average'] = sum(data['lista']) / len(data['lista'])
conn.send(json.dumps(data).encode())
print(f'Server sent the data to the client\n {data}')
