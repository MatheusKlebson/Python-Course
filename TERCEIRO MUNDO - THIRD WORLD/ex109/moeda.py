def diminuir(preço=0,taxa=0,formato=False):
    resp = preço - (preço*taxa/100)
    if formato == False:
        return resp 
    else:
        moeda(resp)
        return resp

def aumentar(preço=0,taxa=0,formato=False):
    resp = preço + (preço*taxa/100)
    if formato == False:
        return resp 
    else:
        moeda(resp)
        return resp


def metade(preço=0,formato=False):
    resp = preço / 2
    if formato == False:
        return resp 
    else:
        moeda(resp)
        return resp

def dobro(preço=0,formato=False):
    resp = preço * 2
    if formato == False:
        return resp 
    else:
        moeda(resp)
        return resp
    
def moeda(preço=0,moeda="R$",formato=False):
    return f"{moeda}{preço:.2f}".replace(".",",")

def resumo(preço=0,taxamais=0,taxamenos=0):
    print("="*50)
    print("{:^50}".format("ANALISANDO O VALOR"))
    print("="*50)
    produtos = ("PREÇO ANALISADO",
            "DOBRO",
            "METADE",
            f"AUMENTO DE {taxamais}%",
            f"DESCONTO DE {taxamenos}"
            ) 
    preços = (preço,dobro(preço),metade(preço),aumentar(preço),diminuir(preço)) 
    for tabela in range(0, len(produtos)): #Laço de repetição que permite formar a tabela
        print(f"{produtos[tabela]:.<40}: R${preços[tabela]:8.2f}")
    '''print(f"A metade de {moeda.moeda(preço)} é {moeda.metade(preço,False)}")
    print(f"O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço,True)}")
    print(f"O aumento de 10%, fica {moeda.aumentar(preço,10,True)}")'''