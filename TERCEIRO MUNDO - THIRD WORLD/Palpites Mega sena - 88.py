# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA  
# criar palpites.O programa vai perguntar quantos jogos serão gerados 
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
sorteados = []
jogos = []
print("="*30)
print("{:^30}".format("PALPITES DA MEGA SENA"))
print("="*30)
totjogos = int(input("QUANTOS JOGOS DESEJA SORTEAR: "))
tot = 0
while tot < totjogos:
    cont = 0
    while True:
        numeros = randint(1,60)
        if numeros not in sorteados: 
            sorteados.append(numeros)
            cont += 1
        if cont == 6:
            break
    tot += 1
    jogos.append(sorteados[:])
    sorteados.clear()
for indice,lista in enumerate(jogos):
    print(f"JOGO {indice}: {sorted(lista)}")
    sleep(1)