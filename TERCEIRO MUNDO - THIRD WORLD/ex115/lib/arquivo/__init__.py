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
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]}{dado[1]}")
    finally:
        a.close()


def cadastrar(arq,nome="desconhecido",idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Ocorreu um ERRO ao tentar abrir o arquivo")
    else:
        try:
           a.write(f"{nome};{idade}\n")
        except:
            print("Ocorreu um ERRO ao adicionar os dados")
        else:
            print(f"{nome} foi cadastrado com sucesso!")
            a.close()
