def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
        return True
    except FileExistsError:
        return False