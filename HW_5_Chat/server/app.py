import socket
import json
from lib.action import Action
from lib.user import User

HOST = "localhost"
PORT = 7777
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST, PORT))
serverSocket.listen()
conn, addr = serverSocket.accept()
data = json.loads(conn.recv(1024))
action = Action(data["type"], User(data["target"]["nickname"]))

if  action.type == "SIGNIN":
    print("User has logged in")
    conn.send(Action("Success").toJSON().encode())
print("Client sent:", data)
print("SERVER FINESHED")
