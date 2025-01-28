from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

#Criptografia Simétrica
def cripto_sim(mensagem, chave):
    cifra = AES.new(chave, AES.MODE_CBC)
    iv = cifra.iv
    texto_enc_sim = cifra.encrypt(mensagem)

    return iv + texto_enc_sim

def decripto_sim(texto_enc_sim, chave):
    iv = texto_enc_sim[:AES.block_size]
    texto_enc_sim = texto_enc_sim[AES.block_size:]

    cifra = AES.new(chave, AES.MODE_CBC, iv=iv)
    texto_dec_sim = cifra.decrypt(texto_enc_sim)

    return texto_dec_sim

chave_sim = get_random_bytes(16)

mensagem = b'Mensagem secreta'

texto_enc_sim = cripto_sim(mensagem, chave_sim)
texto_dec_sim = decripto_sim(texto_enc_sim, chave_sim)

print("---- Criptografia Simétrica ----")
print(f"{texto_enc_sim}\n")
print(f"{texto_dec_sim}\n")

#Criptografia Assimétrica
def gerar_rsa():
    chave_priv_asim = RSA.generate(2048)
    chave_pub_asim = chave_priv_asim.publickey()

    return chave_pub_asim, chave_priv_asim

def cripto_asim(mensagem, chave_publica):
    cifra = PKCS1_OAEP.new(chave_publica)
    texto_enc_asim = cifra.encrypt(mensagem)

    return texto_enc_asim

def decripto_asim(texto_enc_asim, chave_privada):
    cifra = PKCS1_OAEP.new(chave_privada)
    texto_dec_asim = cifra.decrypt(texto_enc_asim)

    return texto_dec_asim

chave_publica, chave_privada = gerar_rsa()

texto_enc_asim = cripto_asim(mensagem, chave_publica)
texto_dec_asim = decripto_asim(texto_enc_asim, chave_privada)

print("---- Criptografia Simétrica ----")
print(f"{texto_enc_asim}\n")
print(f"{texto_dec_asim}\n")
