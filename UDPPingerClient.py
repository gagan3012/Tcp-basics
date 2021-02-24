import time
from socket import *

# PURPOSE:
# The client sends a lowercase message to the server and the client will receive it back captialised.
# The client will send the same message 20 times and set socket timeout for 2 sec, if the server doesn't respond back within 2 sec
# then we return "Request timed out" otherwise return the message captialised and the time it took the server to respond back.

# run the server once, then run the client.


host = 'localhost'
port = 12000

# SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for response from server
clientSocket.settimeout(2)

# Ping ten times
for i in range(1,21):

    # Get the current time.
    currentTime = time.time()

    # store a message to send to the server
    message = 'gagan is my name'

    # Send the message to the server
    clientSocket.sendto(message.encode(), (host, port))

    # If server doesnt respond within the timeout 1 sec, it will through an exception "REQUEST TIMED OUT"
    try:
        # receive message from the server
        data, server = clientSocket.recvfrom(1024)

        # store the time we recevied a response from the server
        responseTime = time.time()

        # get the time it took the server to send a response
        rtt = (responseTime - currentTime)

        # print out the data
        print("Message Received:", data.decode())

        # print the round trip time
        print("Ping " + str(i) + ' ' + str(rtt))

    except timeout:
        print('Request timed out')

# close the socket after it sends 20 packets.
clientSocket.close()
