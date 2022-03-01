#Digite até onde os coelhos devem procriar e contadores
mesFinal = int(input("Até qual mês devo calcular a reprodução dos coelhos?\n"))
count = 1 
anterior = 0
inicio = 1
#Exibe o início e começa o cálculo
print(inicio)
while count < mesFinal:
    proximo = inicio + anterior
    print(proximo)
    anterior = inicio
    inicio = proximo
    count = count + 1
#Exibe o resultado
print("Até o mês descrito( ", mesFinal, ")\nvocê terá", proximo, "casais de coelhinhos")