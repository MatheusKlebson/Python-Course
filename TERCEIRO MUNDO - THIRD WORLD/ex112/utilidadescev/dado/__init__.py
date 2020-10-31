def leiaDinheiro(msg):
    validar = False
    while validar == False:
        preço = str(input(msg)).strip().replace(",",".")
        if preço.isalpha() or preço == "":
            print(f"ERRO!! \"{preço}\" não é um valor")
        else:
            validar = True
            return float(preço)


def leiaInt(message):
    ok = False
    while True:
        n = str(input(message))
        if n.isnumeric():
            int(n)
            ok = True
            break
        else:
            print("ERRO!! VOCÊ NÃO ESCREVEU UM NÚMERO")
    return n
