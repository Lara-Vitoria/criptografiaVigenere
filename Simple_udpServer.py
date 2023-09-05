from socket import *
import json
from vigenere import Vigenere

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))

print ("UDP server\n")

vigenere = Vigenere()

while 1:
    dados, clientAddress = serverSocket.recvfrom(2048)
    dados = json.loads(dados.decode("utf-8"))

    mensagemCriptografada = dados["mensagem"]
    chave = dados["chave"]

    mensagemDescriptografada = vigenere.descriptografa(mensagemCriptografada, chave)

    print ("Mensagem criptografada: ", mensagemCriptografada)
    print ("Mensagem descriptografada: ", mensagemDescriptografada)
    print ("Chave: ", chave)
 