#-*-coding:utf-8;-*-
#Definir uma função (opcional/não solicitado)
def somatoria():
    print("Para sair do programa, digite 0 e pressione ENTER")
    #Solicitar valor ""
    a = int(input("Digite um número inteiro positivo\n"))
    #definir o valor incial da soma
    soma = 0
    #verifica se o valor indicado pelo usuário é maior que 0
    if a > 0:
        #Define um contador
        count = 0
        #Enquanto o contador for menor que 'a'
        while count < a:
            #Soma acresce o contador em seu valor próprio atual (0+1, 1+2, 3+3, 6+4, 10+5 ...)
            soma += count
            #Acrescenta o valor do contador em 1
            count += 1
        #Ao fim do while, imprime a soma total
        print(soma, "\n")
        #Chama novamente a função quando esta acabar (opcional*)
        somatoria()
#invoca a função uma primeira vez
somatoria()