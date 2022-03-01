from socket import *

#Dados do host (ip e porta)
servidor = '127.0.0.1'
porta = 31506 #EL S0G

# AF_INET -> Tipo de identificação com o servidor (usando ip ou hostname)
# SOCK_DGRAM -> Trabalha com o UDP para fazer o broadcast
obj_socket = socket(AF_INET, SOCK_DGRAM)
#Define por onde o serviço deve ser acessado
obj_socket.connect((servidor, porta))
saida = ""
#Enquanto verdadeiro
while saida != "X":
    #Mensagem do cliente
    msg = input('Digite sua mensagem: ')
    #Envio da mensagem para o servidor
    obj_socket.sendto(msg.encode(), (servidor, porta))
    #Recebe a resposta
    dados, origem = obj_socket.recvfrom(65535)
    print('Resposta do servidor: ', dados.decode())
    saida = input('Digite X para sair: ').upper()
#Fechar a conexão
obj_socket.close()