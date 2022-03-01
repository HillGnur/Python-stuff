n = int(input(""))
binario = []

while n >= 1:
    binario.insert(0,n % 2)
    n = n // 2

print(binario)