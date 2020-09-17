#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
palpites = 0
computador = randint(0,10)
print("~"*20)
print("JOGO DA ADIVINHAÇÃO (ENTRE 0 E 10)")
print("="*20)
jogador = int(input("Insira um número: "))
while jogador != computador:
    palpites += 1
    if jogador > computador:
        print("Um número menor...")
    else:
        print("Um número maior...")
    jogador = int(input("Tente novamente, digite um número: "))
print("Total de tentativas: {}".format(palpites))
print(f"O computador pensou no número {computador}")