primos = [2]
n = 2
possibilidades = []
#Altere o limite para o qual você quer calcular
limite = 1000000
#Determinar todos os números primos entre 0 e *limite
while n < limite:
    #Para garantir que o resto da divisão não dê 0 logo de cara, definimos i como sendo um número antecessor a n
    i = n-1
    primo = False
    while (n % i) != 0 and i >= 2:
        if i == 2:
            primo = True
        i-=1
    if primo == True:
        primos.append(n)
        print(n)
    n+=1
#Calcular a soma de primos que resulte no valor limite
for x in primos:
    for y in primos:
        if x + y == limite:
            string = 'A soma de %d e %d é igual a %d'%(x,y,limite)
            possibilidades.append(string)

for z in possibilidades:
    print(z)
