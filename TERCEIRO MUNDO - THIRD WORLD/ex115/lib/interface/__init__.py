def linha(tam=45):
    return "="* tam


def cabeçalho(txt):
    linha()
    print(txt.center(45))
    linha()