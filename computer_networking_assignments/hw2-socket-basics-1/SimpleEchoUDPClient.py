#
# SimpleEchoUDPClient.py
# author : Seung Soo Park ( 20164435 )
#

from socket import *
import time

# serverName = '127.0.0.1'
serverName = 'nsl2.cau.ac.kr'
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
    clientSocket.sendto(sending_message.encode(), (serverName, serverPort))

    # receive result
    # also get current time to calculate duration of sending/receiving moment
    received_message, serverAddress = clientSocket.recvfrom(2048)
    received_time = time.time()

    # print out results
    print('\nReply from server:', received_message.decode())
    print('Response latency =', str((received_time-sending_time) * 1000), 'ms\n')

# function for option 2 : reverse-order
def option_2() :
    # take sending message from user
    sending_message = input('Input sentense: ')

    # send user input to server
    # send with option number so can run proper implement on server as wished
    # also get current time to calculate duration of sending/receiving moment
    sending_message = '2' + sending_message
    sending_time = time.time()
    clientSocket.sendto(sending_message.encode(), (serverName, serverPort))

    # receive result
    # also get current time to calculate duration of sending/receiving moment
    received_message, serverAddress = clientSocket.recvfrom(2048)
    received_time = time.time()

    # print out results
    print('\nReply from server:', received_message.decode())
    print('Response latency =', str((received_time-sending_time) * 1000), 'ms\n')

# function for option 3 : client IP & port
def option_3() :
    # only sends user option value
    # also get current time to calculate duration of sending/receiving moment
    sending_message = '3'
    sending_time = time.time()
    clientSocket.sendto(sending_message.encode(), (serverName, serverPort))

    # receive result
    # also get current time to calculate duration of sending/receiving moment
    received_message, serverAddress = clientSocket.recvfrom(2048)
    received_time = time.time()

    # print out results
    print('\nReply from server:', received_message.decode())
    print('Response latency =', str((received_time-sending_time) * 1000), 'ms\n')

# function for option 4 : server run time
def option_4() :
    # only sends user option value
    # also get current time to calculate duration of sending/receiving moment
    sending_message = '4'
    sending_time = time.time()
    clientSocket.sendto(sending_message.encode(), (serverName, serverPort))

    # receive result
    # also get current time to calculate duration of sending/receiving moment
    received_message, serverAddress = clientSocket.recvfrom(2048)
    received_time = time.time()

    # print out results
    print('\nReply from server:', received_message.decode())
    print('Response latency =', str((received_time-sending_time) * 1000), 'ms\n')

# function for option 5 : terminate client program
def option_5() :
    # only sends user option value
    # also get current time to calculate duration of sending/receiving moment
    print("Bye Bye ~")
    clientSocket.close()

# initial establish for socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# set timeout to socket for 3s
clientSocket.settimeout(5)
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
        elif(client_option_value == 4) :
            option_4()
        elif(client_option_value == 5) :
            option_5()
            break
        else :
            print("inserted wrong option value. \ninsert again\n")
            continue

#uses timeout from socket so that can terminate client when server not responds in 3s.
except timeout :
    print("Server is closed. \nTerminate client side application")
    clientSocket.close()

except KeyboardInterrupt :
    # close connection
    clientSocket.close()
    print("\nBye Bye ~")

except Exception as e :
    # handles all types of error
    print("error name : ", e)
    print("\nunexpected error occred on client. \nTerminate client side application")
    clientSocket.close()