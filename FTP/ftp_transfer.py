from ftplib import *

#Seleciona o servidor ao qual o cliente quer se conectar
ftp = FTP(input('Qual o servidor de FTP? ex.: ftp.example.com.br\n'))
#Recolhe o usuário e senha do cliente
usuario = input('Informe o nome de usuário para login: ')
senha = input('Informe a senha do usuário para login: ')
#Conecta-se ao servidor usando as credenciais informadas
ftp.login(usuario, senha)
#Informa o diretório atual
print('O diretório atual é: ', ftp.pwd())
#Muda para a pasta pública
ftp.cwd('pub')
#Informa o diretório atual
print('O diretório atual é: ', ftp.pwd())
#Lista os diretórios na pasta pública
print(ftp.retrlines('LIST'))
#Encerra a conexão
ftp.quit()