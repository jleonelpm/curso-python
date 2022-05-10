import time

palabra = input("Ingresa una palabra: ")

palabra = palabra.upper()

for letra in palabra:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    else:
        time.sleep(1)
    
    print(letra,end="")