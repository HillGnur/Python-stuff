#--------------#
# Modo usuário #
#--------------#

def pbin(lista, elem, minimo, maximo):
    #Encontrar o meio da lista
    meio = (minimo + (minimo + maximo)) // 2

    if lista[meio] == elem:
        return meio
    elif lista[meio] < elem:
        return pbin(lista, elem, meio, maximo)
    else:
        return pbin(lista, elem, minimo, meio)


#---------------#
# Modo genérico #
#---------------#

#Defina a lista
#listaG = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#Mínimo e máximo genéricos
#minimoG = 0
#maximoG = len(listaG) - 1
#Define função Pesquisa Binária Generalizada
#def pbinG(listaG, elementoG):
    #Define o meio da lista
#   meioG = (minimoG + (minimoG + maximoG)) // 2
    #Caso o elemento no meio seja igual ao procurado, retornar o elemento
#   if listaG[meioG] == elementoG:
#       return meioG
    #Caso o elemento seja maior que a metade da lista, então o mínimo se torna o meio
#   elif listaG[meioG] < elementoG:
#       minimoG = meioG
#       return pbin(listaG, elementoG)
    #Caso o elemento seja menor que a metade da lista, então o máximo se torna o meio
#   else:
#       maximoG = meioG
#       return pbin(listaG, elementoG, minimoG, meioG)