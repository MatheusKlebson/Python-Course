# Exercício Python 107: Crie um módulo chamado moeda.py 
# que tenha as funções incorporadas 
# aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def dicrease(price=0,rate=0):
    response = price - (price*rate/100)
    return response


def increase(price=0,rate=0):
    response = price + (price*rate/100)
    return response


def metade(price=0):
    response = price / 2
    return response


def dobro(price=0):
    response = price * 2
    return response
    