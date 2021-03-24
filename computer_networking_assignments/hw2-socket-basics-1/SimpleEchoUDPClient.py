#
# SimpleEchoUDPClient.py
#

from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
#clientSocket.bind(('', 5432))

print("The client is running on port", clientSocket.getsockname()[1])

message = input('Input lowercase sentence: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print('Reply from server:', modifiedMessage.decode())

clientSocket.close()
