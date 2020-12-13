import socket
import json

HOST = '127.0.0.1'
PORT = 11111


class DataServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self.host, self.port))
        serverSocket.listen()
        conn, addr = serverSocket.accept()
        data = json.loads(conn.recv(1024))
        data['average'] = sum(data['lista']) / len(data['lista'])
        conn.send(json.dumps(data).encode())
        print('Server finished the operation')


server = DataServer(HOST, PORT)
server.start()
