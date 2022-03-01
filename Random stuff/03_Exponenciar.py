#Avisar o usuário sobre o procedimento (opcional)
print("O valor de N será o expoente de X\n")
#solicitar os valores digitados pelo usuário
x = int(input("Digite o valor de X (sendo um inteiro)\n"))
n = int(input("Digite o valor de N (sendo um inteiro positivo)\n"))
#Verificação de número negativo (opcional)
if n < 0:
    n * (-1)
#Imprimir o quadrado
print(x ** n)
