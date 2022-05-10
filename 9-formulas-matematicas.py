import matematicas

print("\nSelecciona una Opción")
print("1.Hipotenusa\n2.Area Circulo\n3.Area de Triangulo (Heron)\n4.Perímetro Triángulo Rectángulo\n5.Salir")
opcion = int(input("Elige la fórmula que deseas calcular: "))

if opcion == 1:
    a = float(input("ingresa el valor de A: "))
    b = float(input("ingresa el valor de B: "))
    c = matematicas.hipotenusa(a,b)
    print("Hipotenusa = ", c)
elif opcion == 2:
    radio = float(input("ingresa el radio de la circunferencia: "))
    area = matematicas.areaCirculo(radio)
    print("Area = ", area)
elif opcion == 3:
    a = float(input("ingresa el valor del lado1: "))
    b = float(input("ingresa el valor del lado2: "))
    c = float(input("ingresa el valor del lado3: "))
    area = matematicas.areaTrianguloHeron(a,b,c)
    print("Area = ", area)
elif opcion == 4:
    a = float(input("ingresa el valor de A: "))
    b = float(input("ingresa el valor de B: "))
    perimetro = matematicas.perimetroTrianguloRectangulo(a,b)
    print("Perimetro = ", perimetro)
else:
    print("La opción que elegiste es incorrecta")



