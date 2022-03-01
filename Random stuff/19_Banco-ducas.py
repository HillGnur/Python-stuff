# encoding: utf-8
#----------------------#
#    Banco de Ducas    #
#----------------------#

#Definindo uma quantidade fixa de notas para trabalhar
notasCem, notasCinq, notasDez, notasCinc, notasUm = 1, 2, 3, 5, 5
#Recebendo o nÃºmero de operaÃ§Ãµes
numOp = int(input("Quantas operaÃ§Ãµes vocÃª pretende realizar?\n"))
#Definindo um contador para laÃ§o de repetiÃ§Ã£o
contador = 0

#Enquanto o contador for menor que o nÃºmero de operaÃ§Ãµes
#----------------------------------------------------------------------#
#  Ex.: Caso 'numOp = 5', contador = 0, 1, 2, 3, 4 - Repetido 5 vezes  #
#----------------------------------------------------------------------#
while contador < numOp:
  #Selecionar o tipo de operaÃ§Ã£o, sendo 0 = saque, e 1 = depÃ³sito
  operacao = int(input("Qual operaÃ§Ã£o deseja efetuar? 0 = saque, 1 = depÃ³sito\n"))

  print("Os valores disponÃ­veis para saque sÃ£o:\n100 ducas: %d\n50 ducas: %d\n10 ducas: %d\n5 ducas: %d\n1 duca: %d\n"%(notasCem, notasCinq, notasDez, notasCinc, notasUm))

  #Verificar se Ã©  saque ou depÃ³sito
  if operacao == 0: #Saque
      
    #Receber o valor a ser sacado
    valorSaque = int(input("Qual valor deseja sacar?\n"))


    #LaÃ§os comparativos para verificar quais os valores sacados e sua quantidade de notas
    #Verifica se Ã© possÃ­vel sacar uma determinada quantia
    if valorSaque <= ((notasCem * 100) + (notasCinq * 50) + (notasDez * 10) + (notasCinc * 5) + (notasUm * 1)):
      #As linhas de cÃ³digo abaixo podem ser refatoradas e comprimidas em uma funÃ§Ã£o
      totalCem, totalCinq, totalDez, totalCinc, totalUm = 0, 0, 0, 0, 0
      # 100 Ducas
      if notasCem > 0:
        totalCem = valorSaque // (notasCem * 100)
        if totalCem > 0:
          valorSaque = valorSaque % (totalCem * 100)
        print(valorSaque)   
      # 50 Ducas
      if notasCinq > 0:
        totalCinq = valorSaque // 50
        if totalCinq > 0:
          valorSaque = valorSaque % (totalCinq * 50)
        print(valorSaque)       
      # 10 Ducas
      if notasDez > 0:
        totalDez = valorSaque // 10
        if totalDez > 0:
          valorSaque = valorSaque % (totalDez * 10)
        print(valorSaque)         
      # 5 Ducas
      if notasCinq > 0:
        totalCinc = valorSaque // 5
        if totalCinc > 0:
          valorSaque = valorSaque % (totalCinc * 5)
        print(valorSaque)      
      # 1 Duca
      if notasUm > 0:
        totalUm = valorSaque // 1
        if totalUm > 0:
          valorSaque = valorSaque % (totalUm * 1)
        print(valorSaque)
                          
      #LaÃ§o de verificaÃ§Ã£o se o valor pÃ´de ser completamente sacado, em seguida, remover as notas do caixa para entregar ao usuÃ¡rio
      if valorSaque == 0:
        #Retirada das notas
        notasCem -= totalCem
        notasCinq -= totalCinq
        notasDez -= totalDez
        notasCinc -= totalCinc
        notasUm -= totalUm
        #Sucesso
        print("Saque realizado com sucesso!\n")
        print("Total de notas sacadas:\n100 ducas: %d\n50 ducas: %d\n10 ducas: %d\n5 ducas: %d\n1 duca: %d\n"%(totalCem, totalCinq, totalDez, totalCinc, totalUm))
        print("Total de notas disponÃ­veis:\n100 ducas: %d\n50 ducas: %d\n10 ducas: %d\n5 ducas: %d\n1 duca: %d\n"%(notasCem, notasCinq, notasDez, notasCinc, notasUm))

      #Caso faltem notas na combinaÃ§Ã£o para sacar o valor Ã­ntegro
      else:
        #Fracasso
        print("A operaÃ§Ã£o nÃ£o pode ser realizada por indisponibilidade de uma combinaÃ§Ã£o de notas")
    else:
      print("A quantia indicada nÃ£o pode ser sacada por ser maior do que a quantia disponÃ­vel")
      print("Total de notas disponÃ­veis:\n100 ducas: %d\n50 ducas: %d\n10 ducas: %d\n5 ducas: %d\n1 duca: %d"%(notasCem, notasCinq, notasDez, notasCinc, notasUm))
            
  elif operacao == 1: #DepÃ³sito

    #Total de notas recebendo um valor total de notas de cada tipo digitados pelo usuÃ¡rio
    notasCem += int(input("Qual a quantidade de notas de 100 (cem) Ducas?\n"))
    notasCinq += int(input("Qual a quantidade de notas de 50 (cinquenta) Ducas?\n"))
    notasDez += int(input("Qual a quantidade de notas de 10 (dez) Ducas?\n"))
    notasCinc += int(input("Qual a quantidade de notas de 5 (cinco) Ducas?\n"))
    notasUm += int(input("Qual a quantidade de notas de 1 (uma) Duca?\n"))

    print("DepÃ³sito efetuado com sucesso!\nSegue abaixo o total de cada nota disponÃ­vel\n")
    print("100 ducas: %d\n50 ducas: %d\n10 ducas: %d\n5 ducas: %d\n1 duca: %d"%(notasCem, notasCinq, notasDez, notasCinc, notasUm))

  else: #Apenas para caso o usuÃ¡rio digite um valor errado, encerra o programa exibindo uma mensagem de erro

    print("O valor digitado Ã© invÃ¡lido, as operaÃ§Ãµes serÃ£o encerradas")
    break
    
  #Acrescer de 1 o contador ao fim do laÃ§o 'while'
  contador += 1
