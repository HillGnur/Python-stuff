import random

def selectSortFn(ListaAleatoria):
  for i in range(len(lista)):
    for j in range(len(lista)):
      if lista[i] < lista[j]:
        lista[j],lista[i] = lista[i],lista[j]
  return lista

lista = []
totalLista = random.randrange(1,20)
for x in range(totalLista):
  lista.append(random.randrange(1,100))

print(lista)
print(selectSortFn(lista))