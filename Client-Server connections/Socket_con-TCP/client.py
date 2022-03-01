from socket import *

#Dados do host (ip e porta)
servidor = '127.0.0.1'
porta = 31506

while True:
    #Mensagem do usuário
    msg = bytes(input('Digite algo: '), 'utf-8')
    # AF_INET -> Tipo de identificação com o servidor (usando ip ou hostname)
    # SOCK_STREAM -> Trabalha com o TCP
    obj_socket = socket(AF_INET, SOCK_STREAM)
    #Define onde o serviço deve se conectar
    obj_socket.connect((servidor, porta))
    #Envia a mensagem
    obj_socket.send(msg)
    #Resposta do servidor
    resposta = obj_socket.recv(1024)
    print("Recebemos: ", resposta.decode())
    #Encerramento da conexão
    obj_socket.close()
