from socket import *

from reward import reward

serverPort = 2000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    rewardout = reward(sentence)
    connectionSocket.send(rewardout.encode())
    connectionSocket.close()
