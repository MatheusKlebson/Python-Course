def diminuir(preço=0,taxa=0,formato=False):
    resp = preço - (preço*taxa/100)
    if formato is False:
        return resp
    else:
        moeda(resp)
        return resp


def aumentar(preço=0,taxa=0,formato=False):
    resp = preço + (preço*taxa/100)
    if formato is False:
        return resp
    else:
        moeda(resp)
        return resp


def metade(preço=0,formato=False):
    resp = preço / 2
    if formato is False:
        return resp
    else:
        moeda(resp)
        return resp


def dobro(preço=0,formato=False):
    resp = preço * 2
    if formato is False:
        return resp
    else:
        moeda(resp)
        return resp
    
def moeda(preço=0,moeda="R$"):
    return f"{moeda}{preço:.2f}".replace(".",",")