import socket
import json
HOST = '127.0.0.1'
PORT = 11111
DATA = {'lista': [10, 20, 35]}

class DataClient:
    def __init__(self, host, port, data):
        self.host = host
        self.data = data
        self.port = port

    def getData(self):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((self.host, self.port))
        clientSocket.send(json.dumps(self.data).encode())
        print(f'Client send data\n {self.data}')
        self.data = json.loads(clientSocket.recv(1024))
        print(f'Client receive new data from server\n {self.data}')

client = DataClient(HOST,PORT,DATA)
client.getData()