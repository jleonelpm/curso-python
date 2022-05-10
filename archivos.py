#Instalar previamente la librería cryptography con: pip3 install cryptography

from cryptography.fernet import Fernet #Importamos el objeto Fernet como método de encriptación asimétrico
from pathlib import Path

def generar_clave():
    """
    Genera una clave y lo almacena en un archivo
    """
    archivo = r"key.key"
    objetoArchivo = Path(archivo)
    if not objetoArchivo.is_file(): #Si no existe el archivo
        clave = Fernet.generate_key()

        with open("key.key", "wb") as key_file:
            key_file.write(clave)

def cargar_clave():
    """
    carga la clave en el directorio actual llamado `key.key`
    """
    return open("key.key", "rb").read()

def encriptar(archivo, clave):
    """
    Encripta un archivo a partir de una clave dada
    """
    f = Fernet(clave)
    with open(archivo, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    datos_encriptados = f.encrypt(file_data)
    # write the encrypted file
    with open(archivo, "wb") as file:
        file.write(datos_encriptados)

def desencriptar(archivo, clave):
    """
    Desencripta un archivo a partir de una clave
    """
    f = Fernet(clave)
    with open(archivo, "rb") as file:
        # read the encrypted data
        datos_encriptados = file.read()
    
    # decrypt data
    datos_encriptados = f.decrypt(datos_encriptados)
    # write the original file
    with open(archivo, "wb") as file:
        file.write(datos_encriptados)

def leerArchivo(archivo):
    stream = open(archivo, "rt", encoding = "utf-8") 
    # se imprime el contenido del archivo
    print(stream.read()) 

def escribirArchivo(linea,archivo):
    with open(archivo, 'a') as file: # argumento a = append o agregar
       file.write("\n"+linea)