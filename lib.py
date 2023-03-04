import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def espera(segundos = 3):
    time.sleep(segundos)

def msg(mensagem, segundos = 4):
    limpar_tela()
    print(mensagem)