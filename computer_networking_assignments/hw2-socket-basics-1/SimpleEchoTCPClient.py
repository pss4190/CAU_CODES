#
# SimpleEchoTCPClient.py
#

from socket import *
from TCPClientFunctions import *

# 127.0.0.1 for localhost ( need to modify into nsl2.cau.ac.kr )
serverName = '127.0.0.1'
serverPort = 24435

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("The client is running on port", clientSocket.getsockname()[1])

# dictionary that contains offering functionalities
offering_functionality = {
    1 : "1) convert text to UPPER-case",
    2 : "2) convert text to reverse order",
    3 : "3) get my IP address and port number",
    4 : "4) get server running time",
    5 : "5) exit"
}

# start Client Application
while True :
    # print out all options that client can choose
    print("<Menu>")
    for key in offering_functionality.keys() :
        print(offering_functionality[key])

    # wait for user's selection input
    print("Input option: ")
    client_option_value = int(input())

    if(client_option_value == 1) :
        print("option_1 start")
        option_1(clientSocket)

message = input('Input lowercase sentence: ')

# send input message to server
clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(2048)
print('Reply from server:', modifiedMessage.decode())

clientSocket.close()