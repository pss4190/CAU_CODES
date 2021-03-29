#
# SimpleEchoUDPServer.py
# author : Seung Soo Park ( 20164435 )
#

from socket import *
import time

serverPort = 24435
BUFFER_SIZE = 2048

# function for option 1 : upper - case
def option_1(received_message, option_value, client_address) :
    # print out requested client address
    print('Connection requested from', client_address)
    print('command', option_value)

    # do action on received message
    modified_message = received_message.upper()
    # send modified message to client
    serverSocket.sendto(modified_message.encode(), client_address)

# function for option 2 : reverse - order
def option_2(received_message, option_value, client_address) :
    # print out requested client address
    print('Connection requested from', client_address)
    print('command', option_value)

    # do action on received message
    msg_length = len(received_message)
    modified_message = ''
    # iterate message from end to start so that can reverse by one single 'for' iteration
    for index in range(msg_length-1, -1, -1) :
        modified_message += received_message[index]

    # send modified message to client
    serverSocket.sendto(modified_message.encode(), client_address)

# function for option 3 : client IP & port
def option_3(option_value, client_address) :
    # print out requested client address
    print('Connection requested from', client_address)
    print('command', option_value)

    # get client IP address & port number from client_address
    client_ip = client_address[0]
    client_port = client_address[1]
    
    modified_message = "client IP = " + str(client_ip) + ", port = " + str(client_port)

    # send message to client
    serverSocket.sendto(modified_message.encode(), client_address)

# function for option 4 : server run time
def option_4(option_value, client_address) :
    # print out requested client address
    print('Connection requested from', client_address)
    print('command', option_value)

    # get current time value so that can get run time of server
    # t_time = time.time() - initializing_time
    run_time = time.strftime('%H:%M:%S', time.gmtime(time.time() - initializing_time))

    # send message to client
    serverSocket.sendto(str(run_time).encode(), client_address)

# server initializing acts
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive on port", serverPort)

# time value to measure run time
initializing_time = time.time()

try :
    while True:
        socket_send_message, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)

        user_option = int(socket_send_message.decode()[0:1])
        user_message = socket_send_message.decode()[1:]

        if(user_option == 1) :
            option_1(user_message, user_option, clientAddress)
        elif(user_option == 2) :
            option_2(user_message, user_option, clientAddress)
        elif(user_option == 3) :
            option_3(user_option, clientAddress)
        elif(user_option == 4) :
            option_4(user_option, clientAddress)
        else :
            print("client send wrong option. \n activation denied")
            continue

        # print('Connection requested from', clientAddress)
        # modifiedMessage = message.decode().upper()
        # serverSocket.sendto(modifiedMessage.encode(), clientAddress)

except KeyboardInterrupt :
    serverSocket.close()
    print("\nBye Bye~")

except Exception as e :
    print("error name : ", e)
    print("\nunexpected error occured on server. \nTerminate server side application.")
    serverSocket.close()