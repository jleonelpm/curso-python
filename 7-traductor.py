diccionario = {
    "amarillo":"yellow", 
    "gato":"cat",  
    "cama":"bed", 
    "lapiz":"pencil", 
    "escribir":"write", 
    "boca":"mouth", 
    "programador":"developer"}

opcion = 0

while opcion != 4:
    print("\nSeleeciona una Opción")
    print("1.Traducir SPA-ENG\n2.Traducir ENG-SPA\n3.Agregar una Palabra\n4.Salir")
    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
        palabra = input("Ingresa la palabra en ESPAÑOL que deseas traducir: ")
        if diccionario.get(palabra)!=None:
            print(palabra, "->", diccionario.get(palabra))
        else:
            print("¡¡¡La palabra que buscas no se encuentra en el diccionario")
    elif opcion == 2:
        palabra = input("Ingresa la palabra en INGLES que deseas traducir: ")
        encontrado = False
        for key in diccionario.keys():
            if palabra == diccionario[key]:
                print(palabra,"->",key)
                encontrado = True
                break
        if encontrado == False:
            print("¡¡¡La palabra que buscas no se encuentra en el diccionario!!!")
    elif opcion==3:
        palabra = input("Ingresa la palabra en ESPAÑOL: ")
        if diccionario.get(palabra)==None:
            traduccion = input("Ingresa la traducción en INGLES")
            diccionario.update({palabra:traduccion})
            print("¡¡¡La palabra se ha agregado al diccionario!!!")
        else:
            print("¡¡¡La palabra que intentas agregar al diccionario ya existe!!!")
    else:
        print("¡¡¡La OPCION que estas eligiendo es INCORRECTA!!!")


