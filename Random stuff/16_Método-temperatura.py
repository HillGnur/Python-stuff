#De fahrenheit para celcius e vice-versa
metodo = input("O que você quer calcular ? (celsius / fahrenheit)")
#Verificar método e executar cálculos
if metodo == "celsius":
    fahrenheit = float(input("Qual a temperatura em fahrenheit?\n"))
    celsius = ((fahrenheit - 32) / 9)
    print("A temperatura convertida em celsius é: ", celsius)
elif metodo == "fahrenheit":
    celsius = int(input())
    fahrenheit = ((celsius * 1.8) + 32)
    print("A temperatura convertida em fahrenheit é: ", fahrenheit)
else:
    print("Você digitou um valor inválido")