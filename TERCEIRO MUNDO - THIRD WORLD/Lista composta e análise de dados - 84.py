#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.
dados = []
pessoas = []
pesado = leve = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        leve = dados[1]
        pesado = dados[1]
    else:
        if leve > dados[1]:
            leve = dados[1]
        if pesado < dados[1]:
            pesado = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
print(f"Total cadastrados foram: {len(pessoas)}")
print(f"Maior peso: {pesado}KG - ",end="")
for p in pessoas:
    if p[1] == pesado:
        print(f"[{p[0]}]",end="")
print(f"\nMenor peso: {leve}KG - ",end="")
for p in pessoas:
    if p[1] == leve:
        print(f"[{p[0]}]",end="")