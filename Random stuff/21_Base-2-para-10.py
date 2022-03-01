b2 = int(input("insira um valor em base 2 \n"))
lista = []
b10 = 0

while b2 > 0:
   lista.append(b2 % 10)
   b2 = b2 // 10
    
for i in range(len(lista)):
    b10 = b10 + (lista[i] * (2 ** i))
    
print(b10)