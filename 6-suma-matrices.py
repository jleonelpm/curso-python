matriz1 = [[1,3,5],[8,9,7],[10,15,90],[21,100,-3]]
matriz2 = [[9,18,15],[81,12,21],[10,15,-3],[1,0,5]]

print("MATRIZ 1 =")
for i in range(len(matriz1)):
    for j in range(len(matriz1[i])):
        print (matriz1[i][j],end="\t")
    print("")

print("MATRIZ 2 =")
for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        print (matriz2[i][j],end="\t")
    print("")

print("RESULTADO = ")
for i in range(len(matriz1)):
    for j in range(len(matriz2[i])):
        resultado = matriz1[i][j] + matriz2[i][j]
        print(resultado, end="\t")
    print("")

        