import random
#Variáveis
m, n = int(input("M")), int(input("N"))
matriz = []
#Appends e geração da Matriz
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(random.randrange(1, 50))
    matriz.append(linha)
#Imprimir a matriz montada
for k in range(len(matriz)):
    print(matriz[k])

cl, cc = len(matriz), len(matriz[0])
print("Linhas: %d;\nColunas: %d;" % (cl, cc))
