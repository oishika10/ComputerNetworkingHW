'''
In this assignment, you will develop a simple Web server in Python that is capable of
processing only one request. Specifically, your Web server will (i) create a connection
socket when contacted by a client (browser); (ii) receive the HTTP request from this
connection; (iii) parse the request to determine the specific file being requested; (iv) get
the requested file from the server file system; (v) create an HTTP response message
consisting of the requested file preceded by header lines; and (vi) send the response
over the TCP connection to the requesting browser. If a browser requests a file that is
not present in your server, your server should return a “404 Not Found” error message.
In the Companion Website, we provide the skeleton code for your server. Your
job is to complete the code, run your server, and then test your server by sending
requests from browsers running on different hosts. If you run your server on a host
that already has a Web server running on it, then you should use a different port than
port 80 for your Web server.
'''

from socket import *

serverName = "OishikaServer"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f'{serverName} server is ready to receive\n')

while True:
    connectionSocket, address = serverSocket.accept()
    print(f'connectionSocket: {connectionSocket}, address: {address}\n')
    try:
        message = connectionSocket.recv(1024).decode()
        print(f'typeof Message:{type(message)},message: {message}\n')
        filename= message.split()[1]
        f = open(filename[1:])
        outputtedData = f.read().replace('\n', ' ')
        statusMessage= 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(statusMessage.encode())
        #Send the output of the requested file to the client
        connectionSocket.send(serverName.encode())
        connectionSocket.send(outputtedData.encode())
        connectionSocket.close()
    except IOError:
        #to be filled
        print(f'IO Error occurred')
        statusMessage = 'HTTP/1.1 404 Resource not found\r\n\r\n'
        connectionSocket.send(statusMessage.encode())
        connectionSocket.close()

serverSocket.close()





