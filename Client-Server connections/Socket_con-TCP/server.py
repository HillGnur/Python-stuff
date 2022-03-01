from socket import *

#Dados do host (ip e porta)
servidor = '127.0.0.1'
porta = 31506 #EL S0G

# AF_INET -> Tipo de identificação com o servidor (usando ip ou hostname)
# SOCK_STREAM -> Trabalha com o TCP
obj_socket = socket(AF_INET, SOCK_STREAM)
#Define por onde o serviço deve ser acessado
obj_socket.bind((servidor, porta))
#Define o máximo de clientes conectados
obj_socket.listen(2)
print('Aguardando o cliente...\n')
#Enquanto verdadeiro
while True:
    #Conexão, cliente, aceita o socket
    con, cliente = obj_socket.accept()
    print('Conectado com: ', cliente)
    #Enquanto verdadeiro
    while True:
        #Recebe mensagem, e em seguida, envia mensagem
        msg_recebida = str(con.recv(1024))
        print('Recebemos: ', msg_recebida.decode())
        msg_enviada = bytes('Olá cliente', 'utf-8')
        con.send(msg_enviada)
        break
    #Fecha a conexão
    con.close()
