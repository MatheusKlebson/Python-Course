def arquivoExite(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except