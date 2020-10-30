def diminuir(preço=0,taxa=0,formato=False):
    resp = preço - (preço*taxa/100)
    return resp if not formato else moeda(resp)


def aumentar(preço=0,taxa=0,formato=False):
    resp = preço + (preço*taxa/100)
    return resp if not formato else moeda(resp)


def metade(preço=0,formato=False):
    resp = preço / 2
    return resp if not formato else moeda(resp)


def dobro(preço=0,formato=False):
    resp = preço * 2
    return resp if not formato else moeda(resp)


def moeda(preço=0,moeda="R$"):
    return f"{moeda}{preço:.2f}".replace(".",",")


def resumo(preço=0,taxaa=10,taxad=5):
    print("="*35)
    print("{:^35}".format("RESUMO DO VALOR"))
    print("="*35)
    print(f"Preço analisado:\t{moeda(preço)}")
    print(f"Dobro do preço:\t\t{dobro(preço,True)}")
    print(f"Metade do preço:\t{metade(preço,True)}")
    print(f"Redução de {taxad}%:\t\t{diminuir(preço,taxad,True)}")
    print(f"Aumento de {taxaa}%:\t\t{aumentar(preço,taxaa,True)}")