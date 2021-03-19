# function for option 1 : upper-case
def option_1(clientSocket) :
    sending_message = input('Input sentense: ')
    clientSocket.send(sending_message.encode())
    received_message = clientSocket.recv(2048)
    print('Reply from server:', received_message.decode())