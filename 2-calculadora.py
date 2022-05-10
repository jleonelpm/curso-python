num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un segundo numero: "))

print("¿Qué operación deseas realizar?")
print("(+)Suma\n(-)Resta\n(*)Multiplicacion\n(/)Division\n(^)Potencia\n(%)Modulo")

opcion = input("Escribe una opción")

if opcion == '+':
    result = num1 + num2
elif opcion == '-':
    result = num1 - num2
elif opcion == '*':
    result = num1 * num2
elif opcion == '/':
    result = num1 / num2
elif opcion == '^':
    result = num1 ** num2
elif opcion == '%':
    result = num1 % num2
else:
    result = "Opcion incorrecta"

print(num1,opcion,num2,"=",result)

