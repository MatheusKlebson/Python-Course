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
    print("="*30)
    print("{:^30}".format("RESUMO DO VALOR"))
    print("="*30)