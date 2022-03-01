import random

def bubbleSortFn(lista):
  for i in range(len(lista) - 1, 0, -1):
    if lista[i] < lista[i - 1]:
      lista[i],lista[i - 1] = lista[i - 1],lista[i]
      return bubbleSortFn(lista)

lista = []
totalLista = random.randrange(1,20)
for x in range(totalLista):
  lista.append(random.randrange(1,100))

print(lista)
print(bubbleSortFn(lista))
