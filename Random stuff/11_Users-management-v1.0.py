#Imports
import datetime, time
##############################
###        Funções         ###
##############################

def login(listaUsers):

  credencial = input("Qual o seu nome reduzido?\n")
  
  if verificaNomesRed(credencial, listaUsers) == False:
  
    usuarioLogado = logarUsuario(credencial, listaUsers)
    boasVindas = "Bem-vindo {}, data de acesso atualizada para {} {}\n".format(usuarioLogado[0], usuarioLogado[4], usuarioLogado[5])
    print(boasVindas)
    catalogo(listaUsers, usuarioLogado)
  
  else:
  
    print("Usuário não existente\n")
    login(listaUsers)

#Logar um usuário
def logarUsuario(credencial, listaUsers):

  for i in range(0 , len(listaUsers)):

    if listaUsers[i][1] == credencial:

      now = datetime.datetime.now()
      listaUsers[i][4] = now.strftime("%m/%d/%Y")
      listaUsers[i][5] = now.strftime("%H:%M")
      return listaUsers[i]

  return False

#Coleta de dados para cadastrar usuário
def coletaDados(usuarioLogado):

  print("Para começarmos o cadastro do usuário, precisamos de algumas informações:\n\n")
  nome = input("Qual o nome do novo funcionário?\n")
  nomeRed = input("Qual o nome reduzido a ser usado?\n")
  cargo = input("Qual o cargo do funcionário?\n")
  permissao = int(input("Qual o nível de permissão deste funcionário?\n\n[0] Visitante\n[1] Usuário\n[2] Administrativo\n[3] Técnico\n[4] Super-usuário\n\n"))
  dataAcesso = "00/00/0000"
  horaAcesso = "00:00"

  if validaDados(nome, nomeRed, cargo, permissao, dataAcesso, horaAcesso, listaUsers) == True:

    print("Os dados de usuário foram validados, prosseguindo com o cadastro...\n")
    cadastroUsuario(nome, nomeRed, cargo, permissao, dataAcesso, horaAcesso, listaUsers, usuarioLogado)

  else:

    print("Devido a este erro, você retornará ao catálogo...\n")
    time.sleep(2)
    catalogo(listaUsers, usuarioLogado)

#Validação de dados para cadastro usando verificação de instância de variável
def validaDados(nome, nomeRed, cargo, permissao, dataAcesso, horaAcesso, listaUsers):

  if isinstance(nome, str) == True:

    if isinstance(nomeRed, str) == True and verificaNomesRed(nomeRed, listaUsers) == True:

      if isinstance(cargo, str) == True:

        if isinstance(permissao, int) == True and permissao >= 0 and permissao <= 4:

          if isinstance(dataAcesso, str) == True:

            if isinstance(horaAcesso, str) == True:

              return True

            else:

              print("Ocorreu um erro, verifique a hora informada\n")
              return False

          else:

            print("Ocorreu um erro, verifique a data informada\n")
            return False

        else:
          print("Ocorreu um erro, por favor verifique a permissão informada\n")
          return False

      else:
        print("Ocorreu um erro, por favor verifique o cargo informado\n")
        return False

    else:
      print("Ocorreu um erro, por favor verifique se o nome reduzido já foi cadastrado\n")
      return False

  else:
    print("Ocorreu um erro, por favor, verifique o nome informado\n")
    return False

#Verificar a duplicidade entre nomes reduzidos
def verificaNomesRed(nomeRed,listaUsers):

  for i in range(0,len(listaUsers)):

    if listaUsers[i][1] == nomeRed:

      return False

  return True

#Cadastrar um novo usuário
def cadastroUsuario(nome, nomeRed, cargo, permissao, dataAcesso, horaAcesso, listaUsers, usuarioLogado):

    usuario = [nome, nomeRed, cargo, permissao, dataAcesso, horaAcesso]
    listaUsers.append(usuario)
    print("Usuário cadastrado com sucesso...\n")
    nome,nomeRed,cargo,permissao,dataAcesso,horaAcesso = None,None,None,None,None,None
    time.sleep(4)
    catalogo(listaUsers, usuarioLogado)

#Filtrar super-usuários e exibir
def superUsers(listaUsers):
  listagemSuperUsers = []
  for i in range(0,len(listaUsers)):
    if listaUsers[i][3] == 4:
      listagemSuperUsers.append(listaUsers[i])
  return listagemSuperUsers

#Pesquisar por nome reduzido
def pesquisaNomeRed(busca, listaUsers):

  for i in range(0,len(listaUsers)):

    if listaUsers[i][1] == busca:

      #Construção de tabela com os dados do usuário
      dadosUsuario = "Nome: {}\nNome red.: {}\nCargo: {}\nPermissao: {}\nÚltima data de acesso: {} {}\n\n".format(listaUsers[i][0], listaUsers[i][1], listaUsers[i][2], listaUsers[i][3], listaUsers[i][4], listaUsers[i][5])
      print("Usuário encontrado, seguem abaixo os dados do usuário:\n\n")
      print(dadosUsuario)
      time.sleep(4)
      return True

  return False

#Remover usuário
def removerUsuario(busca, listaUsers):

  for i in range(0, len(listaUsers)):

    if listaUsers[i][1] == busca:

      del listaUsers[i]
      return True

  return False

#Listagem por níveis de acesso
def listagemAcessos(listaUsers):
  filtroAcesso = []
  for i in range(4,0,-1):
    for n in range(0, len(listaUsers)):
      if listaUsers[n][3] == i:
        filtroAcesso.append(listaUsers[n])
  return filtroAcesso

#Funções para data
#Criar padrão para pesquisa por data
def criarStrData():
  ano = input("Por favor, informe o ANO para a busca (ex.: 1905)\n")
  mes = input("Por favor, informe o MÊS para a busca (ex.: 4, 5, 12)\n")
  dia = input("Por favor, informe o DIA para a busca (ex.: 15, 2, 29)\n")
  #Dia, Mês e Ano
  mda = "{}/{}/{}".format(mes,dia,ano)
  return mda

#Usar padrão para buscar usuários e inserí-los em listagem
def listagemData(listaUsers, mda):
  listagemDt = []
  for i in range(0, len(listaUsers)):
    if listaUsers[i][4].find(mda) == 0:
      print(listaUsers[i][4].find(mda))
      listagemDt.append(listaUsers[i])
  return listagemDt

#Filtrar a lista em ordem
def filtroDt(listagemDt):
  elementos = len(listagemDt) - 1
  ordenado = False
  while not ordenado:
    ordenado = True
    for i in range(elementos):
      if datetime.datetime.strptime(listagemDt[i][5], "%H:%M") > datetime.datetime.strptime(listagemDt[i + 1][5], "%H:%M"):
        listagemDt[i], listagemDt[i + 1] = listagemDt[i + 1], listagemDt[i]
        ordenado = False
        print(listagemDt)
  return listagemDt

#Logout
def logout(listaUsers, usuarioLogado):
  usuarioLogado = None
  login(listaUsers)

################################
####        Catálogo        ####
################################
def catalogo(listaUsers, usuarioLogado):
  
  #Verifica a opção de acordo com o que o usuário digitar
  opcao = int(input("\n\nSelecione a ação desejada:\n0 Cadastro de novo usuário;\n1 Pesquisar usuário (nome reduzido);\n2 Listagem de Super-usuários;\n3 Excluir usuário (nome reduzido);\n4 Listar todos os funcionários (em ordem de nível de permissão);\n5 Listar todos os funcionários (de acordo com data de acesso).\n6 Trocar de usuário\n\n*Caso uma opção inválida seja selecionada, o programa será encerrado\n\n"))
  
  if opcao == 0:
  
    coletaDados(usuarioLogado)
  
  elif opcao == 1:
  
    #Define o termo usado para busca
    busca = input("Qual o nome reduzido?\n")

    if pesquisaNomeRed(busca, listaUsers) == True:
  
      catalogo(listaUsers, usuarioLogado)
  
    else:
  
      print("O usuário {} não foi encontrado.\n".format(busca))
      catalogo(listaUsers, usuarioLogado)

  elif opcao == 2:
    
    listagemSU = superUsers(listaUsers)
    print("Os super-usuários atualmente são %d, sendo eles:"%len(listagemSU))
    for i in range(0, len(listagemSU)):
      print("Nome: {} | Nome red.: {} | Cargo: {} | Último acesso: {} {}".format(listagemSU[i][0], listagemSU[i][1], listagemSU[i][2], listagemSU[i][4], listagemSU[i][5]))
    time.sleep(4)
    catalogo(listaUsers, usuarioLogado)

  elif opcao == 3:
    
    busca = input("Qual o nome reduzido?\n")
    
    if removerUsuario(busca, listaUsers) == True:
    
      print("Usuário removido com sucesso.\n")
      for i in range(0, len(listaUsers)):
        print(listaUsers[i])
      time.sleep(4)
      catalogo(listaUsers, usuarioLogado)
    
    else:
    
      print("O usuário {} não foi encontrado, sendo assim, nenhum registro foi alterado.\n".format(busca))
      catalogo(listaUsers, usuarioLogado)
  
  elif opcao == 4:
    
    listagemAC = listagemAcessos(listaUsers)
    for i in range(0, len(listagemAC)):
      print("Nome: {} | Nome red.: {} | Cargo: {} | Permissão: {} | Último acesso: {} {}".format(listagemAC[i][0], listagemAC[i][1], listagemAC[i][2], listagemAC[i][3], listagemAC[i][4], listagemAC[i][5]))
    time.sleep(4)
    catalogo(listaUsers, usuarioLogado)
  
  elif opcao == 5:
  
    mda = criarStrData()
    listaDt = listagemData(listaUsers, mda)
    listaDtF = filtroDt(listaDt)

    if len(listaDtF) > 0:

      for i in range(0, len(listaDtF)):

        print("Nome: {} | Nome red.: {} | Cargo: {} | Permissão: {} | Último acesso: {} {}".format(listaDtF[i][0], listaDtF[i][1], listaDtF[i][2], listaDtF[i][3], listaDtF[i][4], listaDtF[i][5]))

    else:

      print("Nenhum registro encontrado")

    time.sleep(4)
    catalogo(listaUsers, usuarioLogado)
  
  elif opcao == 6:
  
    logout(listaUsers, usuarioLogado)
  
  #Caso a opção inserida não exista, ele retornará um erro e reiniciará o catálogo
  else:
  
    print("O valor inserido não corresponde a nenhuma opção disponível, o programa será encerrado...\n")
    time.sleep(2)
    exit()

################################
###    Início do programa    ###
################################

#Usuários padrão
listaUsers = [["root", "root", "Administrador do sistema", 4, "00/00/0000", "00:00"], ["technician", "tech", "Técnico encarregado", 3, "00/00/0000", "00:00"], ["management", "admin", "Setor administrativo", 2, "00/00/0000", "00:00"], ["user", "user", "Usuário de sistema", 1, "00/00/0000", "00:00"], ["visitor", "visitor", "Visitante", 0, "00/00/0000", "00:00"]]

print("Para iniciar, temos alguns usuários padrão:")
for i in range(0, len(listaUsers)):
  print(listaUsers[i])
#Inicia o programa
login(listaUsers)
