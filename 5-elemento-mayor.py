miLista = [1002, 17,3,11,5,1,1000,9,15,13,256]

mayor=miLista[0]

for i in range(1,len(miLista)):
    if miLista[i] > mayor:
        mayor = miLista[i]

print(mayor)