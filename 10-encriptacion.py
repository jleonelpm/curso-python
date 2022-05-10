import archivos

opcion = 0

archivos.generar_clave()
clave = archivos.cargar_clave()

archivo = "archivo.txt"

while opcion != 5:

    #print(diccionario)

    print("\nSelecciona una Opción")
    print("1.Leer Archivo\n2.Agregar Texto al Archivo\n3.Encriptar\n4.Desencriptar\n5.Salir")
    opcion = int(input("Ingresa una opción: "))
	
    if opcion == 1:
        print("\nContenido del archivo", "\"" + archivo + "\"")
        archivos.leerArchivo(archivo)
    elif opcion == 2:
        linea = input("Introduce el texto que deseas agregar al archivo: ")
        archivos.escribirArchivo(linea,archivo)
        print("\n¡¡¡Archivo modificado correctamente!!!")
    elif opcion == 3:
        archivos.encriptar(archivo,clave)
        print("\n¡¡¡Archivo encriptado correctamente!!!")
    elif opcion == 4:
        archivos.desencriptar(archivo,clave)
        print("\n¡¡¡Archivo desencriptado correctamente!!!")
    else:
        print("\n¡¡¡La Opción Seleccionada es Incorrecta!!!")
