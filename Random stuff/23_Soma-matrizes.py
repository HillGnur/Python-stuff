import random
#Cria uma matriz com base em M e N definidos pelo usuário
def criaMatrizQ():
  m, n = int(input("M")), int(input("N"))
  matriz = []
  #Popula a matriz com números aleatórios
  for i in range(m):
    linha = []
    for j in range(n):
      linha.append(random.randrange(1, 100))
    matriz.append(linha)
    return matriz
#Cria duas matrizes
a = criaMatrizQ()
b = criaMatrizQ()
#Exibe-as e inicia a matriz vazia C
print(a,b)
c = []
#Verifica se as matrizes são iguais em Mn e Nn, caso sejam, a soma é realizada
if len(a) == len(b) and len(a[0]) == len(b[0]):
  for g in range(len(a)):
    linha = []
    for h in range(len(a[0])):
      linha.append(a[g][h] + b[g][h])
    c.append(linha)
#Exibe o produto da soma de matrizes
print(c)