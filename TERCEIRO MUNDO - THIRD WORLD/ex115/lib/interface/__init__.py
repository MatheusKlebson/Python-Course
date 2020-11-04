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
    opc = leiaInt("Sua opção: ")
    return opc


def leiaInt(mensagem):
    while True:
        try:
            num = int(input(mensagem))
        except (ValueError,TypeError):
            print("ERRO!! Por favor digite um valor inteiro...")
        except (KeyboardInterrupt):
            print("O usuário interropeu o programa, o valor será nulo.")
            return 0
        else:
            return num
            break