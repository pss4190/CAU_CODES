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

serverPort = 24435
BUFFER_SIZE = 2048

# variables for managing client connection thread
clients = {}
client_num = 0

locked = threading.Lock()
stopped = threading.Event()

# function for option 1 : upper-case
def option_1(received_message, option_value, connectionSocket):
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
    print('command', option_value)

    # do action on received message
    modified_message = received_message.upper()
    # send modified message to client
    connectionSocket.send(modified_message.encode())

# function for option 2 : reverse-order
def option_2(received_message, option_value, connectionSocket):
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
    print('command', option_value)

    # do action on received message
    msg_length = len(received_message)
    modified_message = ''
    # iterate message from end to start so that can reverse by one single 'for' iteration
    for index in range(msg_length-1, -1, -1):
        modified_message += received_message[index]

    # send modified message to client
    connectionSocket.send(modified_message.encode())

# function for option 3 : client IP & port
def option_3(option_value, connectionSocket):
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
    print('command', option_value)

    # get client IP address & port number from clientAddress
    client_info = connectionSocket.getpeername()
    client_ip = client_info[0]
    client_port = client_info[1]

    modified_message = "client IP = " + \
        str(client_ip) + ", port = " + str(client_port)

    # send message to client
    connectionSocket.send(modified_message.encode())

# function for option 4 : server run time
def option_4(option_value, connectionSocket):
    # print out requested client address
    print('Connection requested from', connectionSocket.getpeername())
    print('command', option_value)

    # get current time value so that can get run time
    t_time = time.time() - initializing_time
    run_time = time.strftime('%H:%M:%S', time.gmtime(t_time))

    connectionSocket.send(str(run_time).encode())


# time value to measure run time
initializing_time = time.time()

# server initializing acts
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)

print("The server is ready to receive on port", serverPort)

# prints out number of connected clients for every 1 minutes
def client_num_print_thread(clients):
    if not stopped.isSet():
        message = "connected clients : " + str(len(clients))
        print(message)
        client_number_print_thread = threading.Timer(
            60, client_num_print_thread, [clients])
        client_number_print_thread.daemon = True
        client_number_print_thread.start()


def client_thread_activation(connectionSocket, clientAddress, number):
    while not stopped.isSet():
        try:
            # get message from client
            socket_send_message = connectionSocket.recv(BUFFER_SIZE)

            # divide message into selection option and actual message.
            user_option = int(socket_send_message.decode()[0:1])
            user_message = socket_send_message.decode()[1:]

            if(user_option == 1):
                option_1(user_message, user_option, connectionSocket)
            elif(user_option == 2):
                option_2(user_message, user_option, connectionSocket)
            elif(user_option == 3):
                option_3(user_option, connectionSocket)
            elif(user_option == 4):
                option_4(user_option, connectionSocket)
            else:
                print("client send wrong option. \n activation denied")
                continue
        except Exception:
            # when client is closed, it disconnect connectionSocket
            locked.acquire()
            del clients[number]
            connectionSocket.close()
            locked.release()
            print("client", number, "disconnected. Number of connected clients = ", str(len(clients)))
            break

# start to print number of clients on server
client_num_print_thread(clients)

while True:
    try:
        (connectionSocket, clientAddress) = serverSocket.accept()
        locked.acquire()
        client_num += 1
        one_client_thread = threading.Thread(target=client_thread_activation, args=(
            connectionSocket, clientAddress, client_num))
        one_client_thread.daemon = True
        one_client_thread.start()
        clients[client_num] = {
            "client_socket": connectionSocket,
            "client_address": clientAddress,
            "client_thread": one_client_thread
        }
        print("client", client_num, "connected.",
              "Number of connected clients = ", str(len(clients)))
        locked.release()

    except KeyboardInterrupt:
        stopped.set()
        # close all connections
        for index in clients.keys() :
            clients[index]["client_thread"].join()
        serverSocket.close()
        print("\nBye Bye~")
        sys.exit()

    except Exception as e:
        # handles all types of error
        print("error name : ", e)
        print("\nUnexpected error occured on server. \nTerminate server side application.")
        for index in clients.keys() :
            clients[index]["client_thread"].join()
        serverSocket.close()
        sys.exit()