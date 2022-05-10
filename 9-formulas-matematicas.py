import matematicas

print("Selecciona una opcion")
print("1.Hipotenusa\n2.Area Circulo\n3.Area Triangulo (Heron)\n4.Perimetro Triangulo Rectángulo")

opcion = int(input("Elige la fórmula que deseas calcular: "))

if opcion == 1:
    a = float(input("Ingresa el valor de A: "))
    b = float(input("Ingresa el valor de B: "))
    c = matematicas.hipotenusa(a,b)
    print("Hipotenusa = ", c)
elif opcion == 2:
    radio = float(input("Ingresa el radio de la circunferencia: "))
    area = matematicas.areaCirculo(radio)
    print("Area = ", area)
elif opcion == 3:
    l1 = float(input("Ingresa el valor del lado 1: "))
    l2 = float(input("Ingresa el valor del lado 2: "))    
    l3 = float(input("Ingresa el valor del lado 3: "))
    area = matematicas.areaTrianguloHeron(l1,l2,l3)
    print("Area = ", area)    
elif opcion == 4:
    base = float(input("Introduce la base del triagulo: "))
    altura = float(input("Introduce la altura del triangulo: "))
    perimetro = matematicas.perimetroTrianguloRectangunlo(base,altura)
    print("Perimetro = ", perimetro)
else:
    print("¡¡¡Lo siento la opcion que elegiste es incorrecta!!!")
