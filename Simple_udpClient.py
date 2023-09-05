from socket import *
import json
from vigenere import Vigenere

serverName = "" 
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)

print("UDP Client\n")

vigenere = Vigenere()

while 1:
    
    mensagem = input("Mensagem a ser criptografada: ")
    if mensagem == "exit":
            break
    
    chave = input("Chave de criptografia: ")
    
    mensagemCriptografada = vigenere.criptografa(mensagem, chave)

    dados = {
          "mensagem": mensagemCriptografada,
          "chave": chave
    }
    dados_serializados = json.dumps(dados)

    clientSocket.sendto(bytes(dados_serializados, "utf-8"), (serverName, serverPort))

clientSocket.close()