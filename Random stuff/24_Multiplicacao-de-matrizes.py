#Imports
import random

#Variáveis:
#a,b,c = matrizes
#matriz = matriz a ser criada, printada
#m,n,x,y = define linhas e colunas de uma matriz
#g,i,j,k,l = contadores

#Funções de criação e print de matrizes
def criaMatriz():
    m, n = int(input("M")), int(input("N"))
    matriz = []

    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(random.randrange(1,100))
        matriz.append(linha)
    return matriz
def printaMatriz(matriz):
    for p in range(len(matriz)):
        print(matriz[p])

#Criar as matrizes
a = criaMatriz()
b = criaMatriz()
c = [[0 for x in range(len(b[0]))] for y in range(len(a))]

#Verificação de possibilidade de produto
if len(a[0]) == len(b):
    print('O produto das matrizes é: \n')

    #Percorre as linhas de A
    for g in range(len(a)):
        #Percorre as colunas de B
        for k in range(len(b[0])):
            #Percorre as colunas de A
            for l in range(len(a[0])):

                #Soma acumulada do produto de AxB para C
                c[g][k]+=(a[g][l] * b[l][k])

    #Print da Matriz C com os valores finais
    printaMatriz(c)
else:

    #Caso não seja possível, informar ao usuário
    print('Como Aj != Bi, não é possível calcular o produto das matrizes')