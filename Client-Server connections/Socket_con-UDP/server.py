from socket import *

#Dados do host (ip e porta)
servidor = '127.0.0.1'
porta = 31506 #EL S0G

# AF_INET -> Tipo de identificação com o servidor (usando ip ou hostname)
# SOCK_DGRAM -> Trabalha com o UDP para fazer o broadcast
obj_socket = socket(AF_INET, SOCK_DGRAM)
#Define por onde o serviço deve ser acessado
obj_socket.bind((servidor, porta))
print('Servidor pronto...\n')
#Enquanto verdadeiro
while True:
    #Recieve from range máximo de portas
    dados, origem = obj_socket.recvfrom(65535) #Retorna a tupla com os bytes (dados) e a origem
    #Exibição dos dados
    print('Origem: ', origem)
    print('Dados recebidos: ', dados.decode())
    #Envia uma resposta para a origem
    resposta = input('Digite a resposta: ')
    obj_socket.sendto(resposta.encode(), origem)
#Fechar a conexão
obj_socket.close()