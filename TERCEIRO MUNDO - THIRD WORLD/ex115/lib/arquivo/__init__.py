from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt") #rt == ler texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, "wt+") #wt+ cria arquivo
        a.close()
    except:
        print("ERRO. ARQUIVO NÃO PODE SER CRIADO")
    else:
        print(f"Arquivo {nome} foi criado com sucesso")
    

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler arquivo.")
    else:
        cabeçalho('Vendo pessoas cadastradas')
        print(a.read())