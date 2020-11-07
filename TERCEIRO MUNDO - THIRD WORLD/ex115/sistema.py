from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "dadosPessoas - ex115.txt"

if not arquivoExiste(arq):
    criarArquivo("dadosPessoas - ex115.txt")

while True:
    resposta = menu(["VER PESSOAS CADASTRADAS","CADASTRAR PESSOAS","SAIR DO SISTEMA"])
    if resposta == 1:
        #Opção para ver pessoas cadastradas
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastrar uma nova pessoa
        cabeçalho('CADASTRO DE UMA NOVA PESSOA')
        nome = str(input("Nome: ")).strip().title()
        idade = leiaInt("Idade: ")
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        #Opção para sair do sistema
        cabeçalho("Saindo do sistema... Até a próxima")
        break
    else:
        print("ERRO. DIGITE UMA OPÇÃO VÁLIDA")
    sleep(2)