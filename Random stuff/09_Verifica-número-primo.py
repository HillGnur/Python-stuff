#coleta do número a ser verificado
n = int(input("Qual o número a ser verificado?\n"))
#array/lista com os primeiros números primos
primos = [3,5,7,11]
#contadores
i = 0
count = 0
#for para varredura de array e verificação de módulo
for i in range(len(primos)):
    if (n % primos[i]) != 0:
        count += 1
    i += 1
#if e else para verificação do resultado final
if count == 4 or n == 11 or n == 7 or n == 5 or n == 3:
    print("%d é um número primo"%n)
else:
    print("%d não é um número primo"%n)

#Não é a solução apresentada/solicitada pelo professor, é apenas uma alternativa
