#Receber valores
a,b = int(input("qual o valor de A?")),int(input("qual o valor de B?"))
#Verificar maior e reposicionar
if a > b:
    print("o valor de A é %d, sendo A o maior número"%a)
elif a < b:
    print("o valor de B é %d, sendo B o maior número"%b)
else:
    print("os valores digitados são iguais")