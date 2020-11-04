def linha(tam=45):
    return "=" * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())


def menu(lista):
    cabeçalho("MENU DO SISTEMA")
    for i,opções in enumerate(lista):
        print(f"{i + 1} - {opções}")
    print(linha())