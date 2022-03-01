#Variáveis
a,b = int(input("Digite o valor de A\n")), int(input("Digite o valor de B\n"))
print("Os valores de A e B são respectivamente:\n", a, "\n", b)
print("Estamos trocando os valores, aguarde um momento...\n")
#Troca
a,b=b,a
print("Os novos valores de A e B foram redefinidos para:\n", a, "\n", b)