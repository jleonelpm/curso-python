diccionario = {"amarillo":"yellow", "gato":"cat",  "cama":"bed", "lapiz":"pencil", "escribir":"write", "boca":"mouth", "programador":"developer"}

opcion = 0
while opcion != 5:

    #print(diccionario)

    print("\nSelecciona una Opción")
    print("1.Traducir SPA-ENG\n2.Traducir ENG-SPA\n3.Agregar Palabra\n4.Corregir Palabra\n5.Salir")
    opcion = int(input("Ingresa una opción: "))
	
    if opcion == 1:
        palabra = input("Ingresa la palabra a traducir: ")
        if diccionario.get(palabra)!= None:
            print(palabra, "->", diccionario.get(palabra))
        else:
            print("¡¡¡La palabra que buscas no se encuentra en el diccionario!!!")
    elif opcion == 2:
        palabra = input("Ingresa la palabra a traducir: ")
        encontrado = False
        for key in diccionario.keys():
            if palabra == diccionario[key]:
                print(palabra, "->", key)
                encontrado = True
                break
        if encontrado == False:
            print("¡¡¡La palabra que buscas no se encuentra en el diccionario!!!")

                
    elif opcion == 3:
        palabra = input("Ingresa la palabra en español: ")
        if diccionario.get(palabra)== None:
            traduccion = input("Ingresa su traduccion al inglés: ")
            diccionario.update ({palabra:traduccion})
            print("¡¡¡La palabra se ha agregado al diccionario!!!")
        else:
            print("¡¡¡La palabra que intentas agregar ya existe!!!")

