#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador = randint(0,5)
print("~"*50)
print("JOGO DA ADIVINHAÇÃO(0 A 5)")
print("~"*50)
jogador = int(input("Digite um palpite: "))
if jogador == computador:
    print("Voce acertou!!O computador realmente pensou no número",computador)
else:
    print("Voce errou!!O computador pensou no",computador)
