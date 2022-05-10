def esPrimo(num):
    cont = 0
    if num > 1:
        cont = 1
        for i in range(2,num+1):
            if num % i == 0:
                cont = cont + 1
                if cont == 3:
                    break
    if cont == 2:
        result = True
    else:
        result = False
    
    return result

# Cuerpo principal de nuestro programa

for i in range(1,100):
    if esPrimo(i):
        print(str(i) + " es primo")