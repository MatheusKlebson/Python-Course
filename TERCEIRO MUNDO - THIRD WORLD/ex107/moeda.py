# Exercício Python 107: Crie um módulo chamado moeda.py 
# que tenha as funções incorporadas 
# aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def diminuir(preço=0,taxa=0):
    resp = preço - (preço*taxa/100)
    return resp


def aumentar(preço=0,taxa=0):
    resp = preço + (preço*taxa/100)
    return resp


def metade(preço=0):
    resp = preço / 2
    return resp


def dobro(preço=0):
    resp = preço * 2
    return resp
    