import socket, sys
print('Client Server...')

#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)

#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = "127.0.0.1"
name = input('Enter Client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')

while True:
    message = soc.recv(1024)
    message = message.decode()
    print(server_name, ">", message)
    message = input(str("Me > "))

    if message == "[bye]":
        message = "Leaving the Chat room"
        soc.send(message.encode())
        print("\n")
        break

    soc.send(message.encode())