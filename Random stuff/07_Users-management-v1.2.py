#importação de módulos extras
import datetime, json, os.path

#####################################
#    Métodos para uso do arquivo    #
#####################################

def loadJSON(arquivo):
    with open(arquivo) as resultado:
        return json.load(resultado)

def writeJSON(obj, arquivo):
    with open(arquivo, 'w') as resultado:
        return json.dump(obj, resultado)

####################################
#    Funções de uso do programa    #
####################################

#Função de acesso() garante que apenas um usuário logado realize as alterações
def acesso(usuarios, chave):
    usuario = usuarios.get(chave)
    if usuario == None:
        login = input("Usuário incorreto, tente novamente:\n")
        acesso(usuarios, login)
    else:
        print("Bem vindo " + usuario[0])

        print('\n\n')
        menu(usuarios)

#Função Menu(), disponibilizando as opções e direcionando o usuário pelo programa
def menu(usuarios):
    opt = input("Selecione a opção desejada:\nI - Inserir um novo usuário no sistema\nP - Pesquisar um determinado usuário (nome reduzido)\nA - Listagem por acesso\nD - Listagem por data de acesso\nT - Trocar de usuário\nS - Sair do programa\nL - Listar todos os usuários (sem filtros de exibição)\nE - Excluir um usuário (nome reduzido)\n").upper()
    if opt == "I":
        criarUsuario(usuarios, input("Qual o nome reduzido do novo usuário?\n"))
    elif opt == "P":
        pesquisarUsuario(usuarios, input("Qual o nome reduzido do usuário?\n"))
    elif opt == "A":
        print("Listando usuários por ordem crescente de permissões de acesso...\n")
        listagemAcessos(usuarios)
        print("\nListagem completa, retornando ao menu principal\n")
    elif opt == "D":
        mda = criarStrData()
        listagemData(usuarios, mda)
    elif opt == "T":
        acesso(usuarios, input("Digite o usuário a ser acessado:\n"))
    elif opt == "S":
        exit()
    elif opt == "L":
        listagem(usuarios)
    elif opt == "E":
        excluirUsuario(usuarios, input("Digite o nome reduzido do usuário a ser excluído\n"))
    else:
        opt = input("Opção inválida, pressione R para retornar ao menu ou qualquer outra tecla para encerrar o programa\n").upper()
        if opt == "R":
            print('\n\n')
            menu(usuarios)
        else:
            quit()

#Criação de usuários
def criarUsuario(usuarios, chave):
    lista = usuarios.get(chave)
    if lista != None:
        print("Já existe um usuário com o nome reduzido escolhido, retornando ao menu\n")
    else:
        usuarios[chave]=[
            input("Qual o nome completo do novo usuário?\n"),
            input("Qual o cargo deste novo usuário?\n"),
            int(input("Qual o tipo de acesso deste usuário?\n0 - visitante\n1 - usuário\n2 - administrativo\n3 - técnico\n4 - superusuário\n")),
            #A data é tratada separadamente para que haja uma fácil tratativa dos dados ao usar filtros
            [
                datetime.datetime.now().strftime("%m/%d/%Y"),
                datetime.datetime.now().strftime("%H:%M")
            ]
        ]
        writeJSON(usuarios, "users.json")
        print("Usuário cadastrado com sucesso, retornando ao menu\n")
    print('\n\n')
    menu(usuarios)

#Pesquisa de usuários por nome reduzido
def pesquisarUsuario(usuarios, chave):
    lista = usuarios.get(chave)
    if lista != None:
        print("Nome: "+lista[0])
        print("Cargo: "+lista[1])
        print("Tipo de acesso: "+str(lista[2]))
        print("Último acesso: "+lista[3][0]+" "+lista[3][1])
    else:
        print("O usuário informado não existe, você será redirecionado para o menu\n")
    print('\n\n')
    menu(usuarios)

#Listar o dicionário
def listagem(usuarios):
    for chave, valor in usuarios.items():
        print({chave: valor})
    print('\n\n')
    menu(usuarios)

#Excluir usuário
def excluirUsuario(usuarios, chave):
    lista = usuarios.get(chave)
    if lista != None:
        del usuarios[chave]
        print("Usuário excluído com sucesso, retornando ao menu principal\n")
        writeJSON(usuarios, "users.json")
    else:
        print("O usuário escolhido não existe, retornando ao menu principal\n")
    print('\n\n')
    menu(usuarios)

#Listagem por níveis de acesso
def listagemAcessos(usuarios):
    for i in range(4,0,-1):
        for chave, valor in usuarios.items():
            if valor[2] == i:
                print(usuarios[chave])
    print('\n\n')
    menu(usuarios)

#Criar padrão para pesquisa por data
def criarStrData():
    ano = input("Por favor, informe o ANO para a busca (ex.: 1905)\n")
    mes = input("Por favor, informe o MÊS para a busca (ex.: 04, 05, 12)\n")
    dia = input("Por favor, informe o DIA para a busca (ex.: 15, 02, 29)\n")
    #Dia, Mês e Ano
    mda = "{}/{}/{}".format(mes,dia,ano)
    return mda

#Usar padrão para buscar usuários e inserí-los em listagem
def listagemData(usuarios, mda):
    for chave, valor in usuarios.items():
        if valor[3][0].find(mda) == 0:
            print({chave: valor})
    print('\n\n')
    menu(usuarios)

###################################
#    Inicialização do programa    #
###################################

#Preparar o objeto para uso
usuarios = loadJSON('users.json')
#Aquisição do primeiro login do usuário
login = input("Digite seu nome reduzido para fazer login\n")
#Realização do acesso
acesso(usuarios, login)
