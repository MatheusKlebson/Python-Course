def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("ERRO. ARQUIVO NÃO PODE SER CRIADO")
    else:
        print(f"Arquivo {nome} foi criado com sucesso")