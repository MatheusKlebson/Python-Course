#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado 
#tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
print("="*50)
print("{:^50}".format("EM PORTUGUÊS"))
print("="*50)
print("{:^50}".format("JOGANDO DADOS"))
print("="*50)
for cont in range(1,5):
    dado = randint(1,6)
    print(f"O jogador {cont} sorteou o número {dado} no dado...") 
    jogadores[f"Jogador {cont}"] = dado
    sleep(1)
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print("="*50)
print("{:^50}".format("RESULTADO FINAL"))
print("="*50)
for indice, valores in enumerate(ranking):
    print(f"{indice + 1}º Lugar: {valores[0]} com o número do dado: {valores[1]} ")
    sleep(1)
print("="*30)
print("{:^30}".format("IN ENGLISH"))

#Outra resolução
players = {"Player 1": randint(1,6),
"Player 2": randint(1,6),
"Player 3": randint(1,6),
"Player 4": randint(1,6)}
print("="*30)
print("{:^30}".format("PLAYING DATA"))
print("="*30)
for result in players.items():
    print(f"The {result[0]}, Data number: {result[1]}")
    sleep(1)
ranking = sorted(players.items(),key=itemgetter(1),reverse=True) 
print("="*30)
print("{:^30}".format("FINAL RANKING"))
print("="*30)
for i, player_date in enumerate(ranking):
    if i == 0:
        print(f"    - {i + 1}st: {player_date[0]}")
    elif i == 1:
        print(f"    - {i + 1}nd: {player_date[0]}")
    elif i == 2:
        print(f"    - {i + 1}rd: {player_date[0]}")
    else:
        print(f"    - {i + 1}th: {player_date[0]}")
    sleep(1)