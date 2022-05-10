from cryptography.fernet import Fernet
from pathlib import Path

#https://www.thepythoncode.com/code/encrypt-decrypt-files-symmetric-python

def leerArchivo(archivo):
    stream = open(archivo,"rt",encoding="utf-8")
    print(stream.read())

def escribirArchivo(linea, archivo):
    with open(archivo,'a') as file: #argumento a = append o agregar
        file.write("\n"+linea)

def generar_clave():
    archivo = r'key.key'
    objetoArchivo = Path(archivo)
    if not objetoArchivo.is_file(): 
        clave = Fernet.generate_key()

        with open("key.key","wb") as key_file:
            key_file.write(clave)

def cargar_clave():
    return open("key.key","rb").read()

def encriptar(archivo,clave):
    f = Fernet(clave)
    with open(archivo,"rb") as file:
        file_data = file.read()

    #Se encriptan los datos del archivos
    datos_encriptados = f.encrypt(file_data)

    with open(archivo,"wb") as file:
        file.write(datos_encriptados)

def desencriptar(archivo,clave):

    f = Fernet(clave)
    with open(archivo,"rb") as file:
        datos_encriptados = file.read()
    
    datos = f.decrypt(datos_encriptados)

    with open(archivo,"wb") as file:
        file.write(datos)
    
