#Definir função (opcional/não solicitado)
def somatoriaPares():
    #coleta de valores ofertados pelo usuário (início e quantidade de números na sequência)
    inicio = int(input("A partir de qual número devo começar?\n"))
    numerosSeguintes = int(input("Devo obter os pares até quantos números após o informado anteriormente? (Calcularei, por exemplo: n=3, s=5/ 3,4,5,6,7,8)\n"))
    #Define um contador
    count = 0
    #"Distância" percorrida (pode ser expressa apenas pela variável 'numerosSeguintes')
    distancia = ((inicio + numerosSeguintes) - inicio)
    #Verificação e atribuição do valor caso o inicio seja impar ou par
    if inicio % 2 == 0:
        valorAtual = inicio
    else:
        valorAtual = 0
    #Verificação dos valores
    while count < distancia:
        inicio = inicio + 1
        #Caso par, acrescentado ao valorAtual
        if (inicio % 2) == 0:
            valorAtual = valorAtual + inicio
        count = count + 1
    #Ao fim da função, imprimir a soma dos pares
    print(valorAtual)
    #Desconsiderar desta linha em diante <<<
    import time
    time.sleep(5)
    somatoriaPares()
somatoriaPares()
