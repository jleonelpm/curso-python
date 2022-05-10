#Calcular hipotenusa

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto: "))

hipotenusa = (cateto_a ** 2 + cateto_b ** 2) ** 0.5

print("La longitud de la hipotenusa es: ", hipotenusa)