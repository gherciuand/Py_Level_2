from lib.user import User
import socket
from lib.action import Action
import json


action = Action("SIGNIN", User("Jodic"))
print(action)

# connect 2 the server
HOST = "localhost"
PORT = 7777
clientSocked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocked.connect((HOST, PORT))

clientSocked.send(action.toJSON().encode())

data = json.loads(clientSocked.recv(1024))
action = Action(data["type"])
print(action)
