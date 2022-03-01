#Solicita o número de ímpares a serem exibidos para o usuário
n = int(input("Quantos números ímpares devo exibir ?\n"))
#Variáveis de controle
count = 0
nAtual = 0
#Variável para ímpares
vetor = []
while count < n:
    #Atualiza o número atual
    nAtual = nAtual + 1
    #Verifica se n tem resto na divisão por 2 (isso garante se é par ou ímpar em números inteiros)
    if (nAtual % 2)  != 0:
        #Adiciona o ímpar ao vetor e +1 no contador
        vetor.append(nAtual)
        count = count + 1
#Exibe todos os ímpares de acordo com o que foi solicitado pelo usuário
print(vetor)
