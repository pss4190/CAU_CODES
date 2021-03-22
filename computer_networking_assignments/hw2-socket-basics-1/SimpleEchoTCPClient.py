#
# SimpleEchoTCPClient.py
#

from socket import *
import time

# 127.0.0.1 for localhost ( need to modify into nsl2.cau.ac.kr )
serverName = '127.0.0.1'
serverPort = 24435

# function for option 1 : upper-case
def option_1() :
    # take sending message from user
    sending_message = input('Input sentense: ')

    # send user input to server
    # send with option number so can run proper implement on server as wished
    # also get current time to calculate duration of sending/receiving moment
    sending_message = '1' + sending_message
    sending_time = time.time()
    clientSocket.send(sending_message.encode())

    # receive result
    # also get current time to calculate duration of sending/receiving moment
    received_message = clientSocket.recv(2048)
    received_time = time.time()

    # print out results
    print('\nReply from server:', received_message.decode())
    print('Response latency =', str((received_time-sending_time) * 1000), 'ms\n')

# function for option 2 : reverse-order
def option_2() :
    # take sending message from user
    sending_message = input('Input sentense: ')

    # send user input to server
    # send with option number so can run proper implement on server
    # also get current time to calculate duration of sending/receiving moment
    sending_message = '2' + sending_message
    sending_time = time.time()
    clientSocket.send(sending_message.encode())

    # receive result
    # also get current time to calculate duration of sending/receiving moment
    received_message = clientSocket.recv(2048)
    received_time = time.time()

    # print out results
    print('\nReply from server:', received_message.decode())
    print('Response latency =', str((received_time-sending_time) * 1000), 'ms\n')

# function for option 3 : client IP & port
def option_3() :
    # only sends user option value
    # also get current time to calculate duration of sending/receiving moment
    sending_time = time.time()
    clientSocket.send("3".encode())

    # receive result
    # also get current time to calculate duration of sending/receiving moment
    received_message = clientSocket.recv(2048)
    received_time = time.time()

    # print out results
    print('\nReply from server:', received_message.decode())
    print('Response latency =', str((received_time-sending_time) * 1000), 'ms\n')

# initial establish connection to server
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

try :
    # start Client Application
    while True :
        # print out all options that client can choose
        print("<Menu>")
        for key in offering_functionality.keys() :
            print(offering_functionality[key])

        # wait for user's selection input
        print("Input option: ", end=' ')
        client_option_value = int(input())

        if(client_option_value == 1) :
            option_1()
        elif(client_option_value == 2) :
            option_2()
        elif(client_option_value == 3) :
            option_3()
        else :
            print("inserted wrong option value. \ninsert again\n")
            continue
except KeyboardInterrupt :
    # close connection
    clientSocket.close()
    print("\nBye Bye~")
except :
    # handles all types of error
    print("\n unexpected error occured on client. \nTerminate client side application.")
    clientSocket.close()