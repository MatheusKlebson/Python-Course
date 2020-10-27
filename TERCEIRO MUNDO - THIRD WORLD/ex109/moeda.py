def diminuir(preço=0,taxa=0,formato=False):
    resp = preço - (preço*taxa/100)
    return resp 


def aumentar(preço=0,taxa=0,formato=False):
    resp = preço + (preço*taxa/100)
    return resp


def metade(preço=0,formato=False):
    resp = preço / 2
    return resp


def dobro(preço=0,formato=False):
    resp = preço * 2
    return resp
    
def moeda(preço=0,moeda="R$",formato=False):
    return f"{moeda}{preço:.2f}".replace(".",",")