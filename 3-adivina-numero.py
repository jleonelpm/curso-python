from random import randrange
numeromagico = randrange(10)
print(numeromagico)

intentos = 0 
win = False

while intentos < 3:
  numero = int(input("Adivina qué número (0 a 9) generó la computadora"))
  if numero == numeromagico:
     win = True
     break
  intentos = intentos + 1

if win == True:
   print("Felidades, Ganaste")
else:
   print("Lo siento, sigue intentando")
