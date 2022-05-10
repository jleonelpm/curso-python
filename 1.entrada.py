algo = input("Dime algo: ")
print("MMMM...", algo, "... ¿En Serio?")


algo = float(input("Inserta un numero: "))
resultado =algo ** 2.0 #Por lo tanto hay que convertirlo
print(algo, "al cuadrado es ", resultado)

#Calcular hipotenusa
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** 0.5
print("La longitud de la hipotenusa es: ", hipo)

#Solicitando tus datos
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

#Pintando un cuadro
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")