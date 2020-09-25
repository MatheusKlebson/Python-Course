#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado 
#tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
print("Valores sorteado...")
for cont in range(1,5):
    dado = randint(1,6)
    print(f"Jogador {cont} tirou {dado} no dado")
    sleep(2)