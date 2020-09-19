#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.
lista = [[],[]]
pesado = 0
leve = 0
cont = 0
while True:
    nome = str(input("Nome da pessoa: "))
    peso = float(input("Peso da pessoa(KG): "))
    lista[0].append(nome)
    lista[1].append(peso)
    while cont <= len(lista):
        if cont == 0:
            pesado = lista[1][cont]
            leve = lista[1][cont]
        else:
            if pesado < lista[1][cont]:
                pesado = lista[1][cont]
            if leve > lista[1][cont]:
                leve = lista[1][cont]
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
print(f"Total cadastrados: {len(lista)}")
print(leve,pesado)