# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA  
# criar palpites.O programa vai perguntar quantos jogos serão gerados 
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
sorteados = []
print("="*30)
print("{:^30}".format("PALPITES DA MEGA SENA"))
print("="*30)
tot = int(input("QUANTOS JOGOS DESEJA SORTEAR: "))
jogos = 0
while jogos <= tot:
    numeros = randint(1,60)
    if len(sorteados) < 6:
        sorteados.append(numeros)
        jogos += 1
    else:
        break
print(sorteados)
 