#Solicitar o valor ao usuário
fatorial = int(input("qual o valor fatorial a ser calculado? ( n! )\n"))
#O fim deve ser igual ao fatorial em primeiro momento, para que possamos usar os dois valores gerados pelo fatorial
final = fatorial
#Enquanto fatorial for maior que 1
while fatorial > 1:
    #Final recebe o valor atual do fatorial e multiplica pelo próximo número
    #Pode ser reescrito >>>  final = final * (fatorial - 1)
    final *= (fatorial - 1)
    #O valor do número atual a ser multiplicado diminui em 1 a cada passo
    fatorial -= 1
#Ao final do processo, imprimir o valor final do fatorial solicitado
print(final)
