import re

opcion = 0
while opcion != 6:

    #print(diccionario)

    print("\nSelecciona una Opción")
    print("1.Buscar Palabra\n2.Buscar Número\n3.Palabras que inicien con Mayúscula\n4.Palabras que inicien con Vocal\n5.Encontrar Numeros\n6.Salir")
    opcion = int(input("Ingresa una opción: "))
	
    if opcion == 1:
        texto = "Curso de Python 3 con Ejemplos"
        print(texto, end="\n")
        regex = input("Ingresa la palabra que deseas encontrar: ")
        if re.search(regex,texto):
            print("La palabra \"" + regex + "\" si se encuentra en el texto")
        else:
            print ("Palabra no encontrada")
    elif opcion == 2:
        texto = input("Escribe un texto: ")
        regex = "\d+"
        if re.search(regex,texto):
            print("Si hay numeros en el texto")
        else:
            print("No hay numeros en el texto")
    elif opcion == 3:
        filename = "loremipsum.txt"
        textfile = open(filename,"r")
        regex = "[A-Z][a-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    elif opcion == 4:
        filename = "loremipsum.txt"
        textfile = open(filename,"r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            regex = "[A-Za-z]+[aeiou]$"
            for elemento in lista:
                if re.search(regex,elemento):
                    print(elemento)
    elif opcion == 5:
        filename = "loremipsum.txt"
        textfile = open(filename,"r")
        regex = "[0-9]{4}"
        reg = re.compile(regex)
        for line in textfile:
            lista = reg.findall(line)
            print(lista)
        textfile.close()
    else:
        print("\n¡¡¡La Opción Seleccionada es Incorrecta!!!")