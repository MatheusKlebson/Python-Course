# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA  
# criar palpites.O programa vai perguntar quantos jogos serão gerados 
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
listas = []
jogos = []
print("="*30)
print("{:^30}".format("PALPITES DA MEGA SENA"))
print("="*30)
totjogos = int(input("Quantos jogos deseja sortear? "))
totcadastros = 0
while totcadastros < totjogos:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in listas:
            listas.append(numero)
            cont += 1
        if cont == 6:
            break
    totcadastros += 1
    jogos.append(listas[:])
    listas.clear()
print("="*30)
print("{:^30}".format("FORMANDO JOGOS"))
print("="*30)
for indice, jogo in enumerate(jogos):
    print(f"JOGO {indice + 1}: {sorted(jogo)}")
    sleep(1)