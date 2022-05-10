from os import strerror

#Procesando archivo caracter por caracter - segundo método
#Recuerda - el leer un archivo muy grande (en terabytes) 
# usando este método puede dañar tu sistema operativo.

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCaracteres en el archivo: ", cnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))