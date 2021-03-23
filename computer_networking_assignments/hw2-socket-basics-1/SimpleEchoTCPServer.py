#
# SimpleEchoTCPServer.py
# author : Seung Soo Park ( 20164435 )
#
from socket import *
from datetime import datetime
import time

# function for option 1 : upper-case
def option_1(received_message, option_value) :
    # print out requested client address
    print('Connection requested from', clientAddress)
    print('command', option_value)

    # do action on received message
    modified_message = received_message.upper()
    # send modified message to client
    connectionSocket.send(modified_message.encode())

# function for option 2 : reverse-order
def option_2(received_message, option_value) :
    # print out requested client address
    print('Connection requested from', clientAddress)
    print('command', option_value)

    # do action on received message
    msg_length = len(received_message)
    modified_message = ''
    # iterate message from end to start so that can reverse by one single 'for' iteration
    for index in range(msg_length-1, -1, -1) :
        modified_message += received_message[index]
    
    # send modified message to client
    connectionSocket.send(modified_message.encode())

# function for option 3 : client IP & port
def option_3(option_value) :
    # print out requested client address
    print('Connection requested from', clientAddress)
    print('command', option_value)

    # get client IP address & port number from clientAddress
    client_ip = clientAddress[0]
    client_port = clientAddress[1]
    print(client_ip, " and ", client_port)

    modified_message = "client IP = " + str(client_ip) + ", port = " + str(client_port)

    # send message to client
    connectionSocket.send(modified_message.encode())

# function for option 4 : server run time
def option_4(option_value) :
    # print out requested client address
    print('Connection requested from', clientAddress)
    print('command', option_value)

    # get current time value so that can get run time
    print("time : ", (time.time() - initializing_time))
    t_time = time.time() - initializing_time
    run_time = time.strftime('%H:%M:%S', time.gmtime(t_time))
    print("run_time created")
    print("time : ", str(run_time))

    connectionSocket.send(str(run_time).encode())

def option_5(option_value) :
    connectionSocket.close()
    print("Bye Bye~")


# time value to measure run time
initializing_time = time.time()
print(initializing_time)
# server initializing acts
serverPort = 24435
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("The server is ready to receive on port", serverPort)
# accept connection requeset from client
(connectionSocket, clientAddress) = serverSocket.accept()

try :
    while True :
        # get message from client
        socket_send_message = connectionSocket.recv(2048)

        # divide message into two pieces : user selection option, and user message
        user_option = int(socket_send_message.decode()[0:1])
        user_message = socket_send_message.decode()[1:]
        print("user option : ", user_option)
        print("user message : ", user_message)

        if(user_option == 1) :
            option_1(user_message, user_option)
        elif(user_option == 2) :
            option_2(user_message, user_option)
        elif(user_option == 3) :
            option_3(user_option)
        elif(user_option == 4) :
            option_4(user_option)
        elif(user_option == 5) :
            option_5(user_option)
            break
        else :
            print("client send wrong option. \n activation denied")
            continue
except KeyboardInterrupt :
    # close the connectioni
    connectionSocket.close()
    print("\nBye Bye~")
except Exception as e:
    # handles all types of error
    print("error name : ", e)
    print("\nUnexpected error occured on server. \nTerminate server side application.")
    connectionSocket.close()