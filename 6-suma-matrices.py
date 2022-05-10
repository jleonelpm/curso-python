matrizA = [[2,3,5],[3,4,7],[9,10,11]]
matrizB = [[12,-1,5],[21,34,0],[10,21-4]]
col = 3
fil = 3
matrizC = []

print("Su primera matriz es:")
for i in range(len(matrizA)):
  for j in range(len(matrizA[i])):
    print(matrizA[i][j], end="\t")
  print("")

print("Su segunda matriz es:")
for i in range(len(matrizB)):
  for j in range(len(matrizB[i])):
    print(matrizB[i][j], end="\t")
  print("")

print("Su tercera matriz (la suma de las dos anteriores) es:")
for i in range(len(matrizA)):
  matrizC.append([])
  for j in range(len(matrizB[i])):
    suma = matrizA[i][j] + matrizB[i][j]
    #matrizC[i].append(suma)
    print(suma, end="\t")
  print("")