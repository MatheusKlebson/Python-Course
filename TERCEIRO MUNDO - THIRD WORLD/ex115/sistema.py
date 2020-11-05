from lib.interface import *
from arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if 
while True:
    resposta = menu(["VER PESSOAS CADASTRADAS","CADASTRAR PESSOAS","SAIR DO SISTEMA"])
    if resposta == 1:
        cabeçalho("Vendo pessoas")
    elif resposta == 2:
        cabeçalho("Cadastrando")
    elif resposta == 3:
        cabeçalho("Saindo do sistema... Até a próxima")
        break
    else:
        print("ERRO. DIGITE UMA OPÇÃO VÁLIDA")
    sleep(2)