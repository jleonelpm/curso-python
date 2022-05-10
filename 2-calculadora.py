num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa un segundo número:"))

print("\n¿Qué operación deseas realizar?")
print("(+)Suma\n(-)Resta\n(*)Multiplicación\n(/)Division\n(^)Potencia\n(%)Módulo")
opcion = input("Selecciona una opción: ")

if opcion == '+':
  result = num1 + num2
elif opcion == '-':
  result = num1 - num2
elif opcion == '*':
  result = num1 * num2
elif opcion == "/":
  result = num1 / num2
elif opcion == "^":
  result = num1 ** num2
elif opcion == "%":
  result = num1 % num2
else:
  result = "Opcion Incorrecta"

print(num1, opcion, num2, "=",result )

