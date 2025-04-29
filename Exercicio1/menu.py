import os
import time
from util.inputPlus import inputPlus
from util.base64 import base64Encode, base64Decode 
from util.sha256Encode import sha256Encode
from util.keyHandler import saveKey, validateKey


def exibirMenu():
    op = 1
    while op:
        os.system('cls')
        print("===== MENU =====")
        print("Escolha: ")
        print("1. Codificar uma mensagem")
        print("2. Decodificar uma mensagem")
        print("0. Sair")
        op = inputPlus("Digite: ", 0, 2)
        
        if op == 1:
            while op:
                os.system('cls')

                print("===== CODIFICAR MENSAGEM =====")
                
                message = input("Digite a mensagem a ser codificada: ")

                base64Encoded = base64Encode(message)
                print("=========================")
                print("Mensagem codificada:", base64Encoded)
                print("=========================")
                saveKey("mensagem", sha256Encode(message, 's'))
                
                print("Deseja codificar outra mensagem?")
                print("1. Sim")
                print("0. Não")

                op = inputPlus("Digite: ", 0, 1)
            op = 1
            
        elif op == 2:
            while op:
                os.system('cls')
                
                print("===== DECODIFICAR =====")

                base64Encoded = input("Digite a mensagem codificada: ")

                base64Decoded = base64Decode(base64Encoded)
                print("Mensagem decodificada:", base64Decoded)
                
                sha256Encoded = sha256Encode(base64Decoded, 's')
                print("=========================")
                validateKey("mensagem", sha256Encoded)
                print("=========================")
                
                print("Deseja decodificar novamente?")
                print("1. Sim")
                print("0. Não")

                op = inputPlus("Digite: ", 0, 1)

                os.system('cls')

            print("Voltando ao menu principal...")

            op = 2

    print("Saindo do programa...")

exibirMenu()