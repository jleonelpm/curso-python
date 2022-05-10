import socket

#AF_INET se refiere a una familia IP
#SOCK_STREAM indica que es una conexión TCP
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Especificamos la dirección ip y el puerto en el cual
#escuchará nuestro servidor
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(5) #Máximo de conexiones

print(f"\n\nServer Listening on {ip}:{port}")

salir = False
while salir == False:
    conexion, address = socket_server.accept()
    print ("La conexión  ha sido establecida")

    while True:
        message = conexion.recv(1024)
        message = message.decode()
        print(message)

        if message == '[exit]':
            message = 'Adios...'
            conexion.send(message.encode())
            print("\n")
            salir = True
            break
        elif message == "hola":
            message = 'Que tal soy el server...'
            conexion.send(message.encode())
        else:
            message = 'No entiendo que deseas...'            
            conexion.send(message.encode())

conexion.close()
print("Servidor Finalizado")
