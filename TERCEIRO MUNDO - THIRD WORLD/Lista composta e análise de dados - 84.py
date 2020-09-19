#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.
lista = []
pessoas = []
pesado = 0
leve = 0

while True:
    lista.append(str(input("Nome da pessoa: ")))
    lista.append(float(input("Peso da pessoa(KG): ")))
    if len(pessoas) == 0:
        pesado = lista[1]
        leve = lista[1]
    else:
        if pesado < lista[1]:
            pesado = lista[1]
        if leve > lista[1]:
            leve = lista[1]
    pessoas.append(lista[:])
    pessoas.clear()
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
print(f"Total cadastrados: {len(pessoas)}")
print(leve,pesado)