import socket
import json

HOST = '127.0.0.1'
PORT = 11111
data = {'lista': [10, 20, 35]}
print('Client STARTED')
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((HOST, PORT))


print('Client>> sendnding the data')
clientSocket.send(json.dumps(data).encode())
data = json.loads(clientSocket.recv(1024))
print(f'Client received calculated data from server\n {data}')
print('Client FINESHED')
