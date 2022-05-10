import time
palabra = input("Ingresa una palabra: ")

# y asignarlo a la variable userWord.
palabra = palabra.upper()

for letra in palabra:
    # Completa el cuerpo del ciclo for.
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    time.sleep(1)
    print(letra,end="")
