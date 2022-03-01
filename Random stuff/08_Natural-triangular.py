#importação de módulo
import string
#coleta o valor a ser verificado para o usuário
n = int(input("Devo verificar qual número?\n"))
def verificaTriangulo(n, string):
    #naturais multiplicadores e variáveis iniciais
    x1,x2,x3 = 2,3,4
    valorTotal = 0
    conjNumeros = []
    #loop de verificação do produto
    while valorTotal < n:
        novoValor = ((x1 * x2) * x3)
        conjNumeros = [x1,x2,x3]
        #Alteração dos valores para dar continuidade ao while
        valorTotal = novoValor
        x1,x2,x3 = x1 + 1, x2 + 1, x3 + 1
    #Caso o novo valor seja maior que N, automaticamente N não é triangular
    if novoValor > n:
        print("O número informado não é triangular")
    else:
        print(valorTotal)
        #conversão dos valores em um array para string (usando 'str()' + um forLoop para coleta de valores), e separação dos valores por vírgula utilizando o método join do módulo string que foi importado
        #print do ângulo + valores naturais consecutivos
        novoConjNumeros = ", ".join(str(i) for i in conjNumeros)
        print(novoConjNumeros, " são os três números naturais")
#chamada da função
verificaTriangulo(n, string)
