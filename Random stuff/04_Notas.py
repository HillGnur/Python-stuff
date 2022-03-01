#O usuário informa o número de alunos totais na sala, em seguida são declaradas as variáveis que complementarão os loops
alunos = int(input("Qual o número de alunos na sala?\n"))
notasAlunos = []
count = 0
#loop de armazenamento de notasXalunos
while count < alunos:
    notaAluno = int(input("Qual a nota do aluno " + str(count + 1) + "? (0 a 100 pontos)\n"))
    notasAlunos.append(notaAluno)
    count = count + 1
#count zerado para ser reutilizado no próximo loop
count = 0
#Variáveis de notas
menorNota = 100
maiorNota = 0
alunosMeN,alunosMaN = 0,0
#loop de verificação do valor de notas (min e max), e verificação de notas mínimas ou máximas iguais
while count < len(notasAlunos):
    if notasAlunos[count] < menorNota:
        alunosMeN = 0
        menorNota = notasAlunos[count]
    if notasAlunos[count] > maiorNota:
        alunosMaN = 0
        maiorNota = notasAlunos[count]
    if notasAlunos[count] == menorNota:
        alunosMeN = alunosMeN + 1
    elif notasAlunos[count] == maiorNota:
        alunosMaN = alunosMaN + 1
    count = count + 1
#print com os valores da maior e menor nota, junto ao número de alunos que tiraram determinada nota
print("A maior nota tirada foi ", maiorNota, " Essa nota foi tirada por ", alunosMaN, " aluno(s)\n")
print("A menor nota tirada foi ", menorNota, " Essa nota foi tirada por ", alunosMeN, " aluno(s)\n")
