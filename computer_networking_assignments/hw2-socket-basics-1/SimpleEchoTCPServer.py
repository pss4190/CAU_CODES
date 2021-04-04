#
# SimpleEchoTCPServer.py
# author : Seung Soo Park ( 20164435 )
#
from socket import *
from datetime import datetime
import time
import select
import threading
import sys
import pickle

serverPort = 24435
socket_list = []
BUFFER_SIZE = 2048

# function for option 1 : upper-case
def option_1(received_message, option_value, connectionSocket) :
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
    print('command', option_value)

    # do action on received message
    modified_message = received_message.upper()
    # send modified message to client
    connectionSocket.send(modified_message.encode())

# function for option 2 : reverse-order
def option_2(received_message, option_value, connectionSocket) :
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
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
def option_3(option_value, connectionSocket) :
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
    print('command', option_value)

    # get client IP address & port number from clientAddress
    client_info = connectionSocket.getpeername()
    client_ip = client_info[0]
    client_port = client_info[1]

    modified_message = "client IP = " + str(client_ip) + ", port = " + str(client_port)

    # send message to client
    connectionSocket.send(modified_message.encode())

# function for option 4 : server run time
def option_4(option_value, connectionSocket) :
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
    print('command', option_value)

    # get current time value so that can get run time
    t_time = time.time() - initializing_time
    run_time = time.strftime('%H:%M:%S', time.gmtime(t_time))

    connectionSocket.send(str(run_time).encode())

# server initializing acts
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

# add serverSocket to socket_list
socket_list.append(serverSocket)

print("The server is ready to receive on port", serverPort)

# time value to measure run time
initializing_time = time.time()

try :
    while True :
        # get socket list through select
        # so that can configure whether to accept new connection or just handle for incoming messages
        read_sockets,write_sockets,error_sockets = select.select(socket_list,[],[])

        for sock_element in read_sockets :
            # if serverSocket is readable ( = there is new connection request )
            if sock_element == serverSocket :
                # accept new connection and add socket to socket_list for handling opened connections
                (new_connect_socket, new_client_addr) = serverSocket.accept()
                socket_list.append(new_connect_socket)
            # if connection sockets are readable ( = there is new received message for socket )
            else :
                try :
                    # get message from client
                    socket_send_message = sock_element.recv(BUFFER_SIZE)

                    # divide message into selection option and actual message.
                    user_option = int(socket_send_message.decode()[0:1])
                    user_message = socket_send_message.decode()[1:]

                    if(user_option == 1) :
                        option_1(user_message, user_option, sock_element)
                    elif(user_option == 2) :
                        option_2(user_message, user_option, sock_element)
                    elif(user_option == 3) :
                        option_3(user_option, sock_element)
                    elif(user_option == 4) :
                        option_4(user_option, sock_element)
                    else :
                        print("client send wrong option. \n activation denied")
                        continue
                except Exception :
                    # when client is closed, it disconnect connectionSocket
                    print("client :", sock_element.getpeername(), "is disconnected")
                    sock_element.close()
                    socket_list.remove(sock_element)

except KeyboardInterrupt :
    # close the connection
    for sock_element in socket_list :
        sock_element.close()
    serverSocket.close()
    print("\nBye Bye~")

except Exception as e:
    # handles all types of error
    print("error name : ", e)
    print("\nUnexpected error occured on server. \nTerminate server side application.")
    for sock_element in socket_list :
        sock_element.close()
    serverSocket.close()