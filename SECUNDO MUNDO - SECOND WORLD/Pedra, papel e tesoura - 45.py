#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
ganhajogador = 0
ganhacomputador = 0
print("="*60)
print("{:^60}".format("GAME: PEDRA, PAPEL E TESOURA"))
print("="*60)
sleep(2)
print('''REGRAS:
1 - Se escolher algum número que não está nas
opções o computador ganhará uma vitória

2 - Se escolher alguma letra o jogo será interropido''')
sleep(5)
while True:
    print(" ")
    print("[PLACAR: Jogador {} X {} COMPUTADOR]".format(ganhajogador,ganhacomputador))
    computador = randint(1,3)
    print(" ")
    jogador = int(input('''SUAS OPÇÕES:
    [1]PEDRA
    [2]PAPEL
    [3]TESOURA
    DIGITE: '''))
    print("Analisando...")
    sleep(3)
    if jogador == 1:
        print("{} escolheu Pedra".format(nome))
        if jogador == computador:
            print("Computador escolheu Pedra")
            sleep(2)
            print("Empate!!")
            print(" ")
        elif computador == 2:
            print("Computador escolheu Papel")
            sleep(2)
            print("Vencedor: Computador")
            print(" ")
            ganhacomputador += 1
        elif computador == 3:
            print("Computador escolheu Tesoura")
            sleep(2)
            print("Vencedor: {}".format(nome))
            print(" ")
            ganhajogador += 1
    elif jogador == 2:
        print("{} escolheu Papel".format(nome))
        if computador == 1:
            print("Computador escolheu Pedra")
            sleep(2)
            print("Vencedor: {}".format(nome))
            print(" ")
            ganhajogador += 1
        elif jogador == computador:
            print("Computador escolheu Papel")
            sleep(2)
            print("Empate!!")
            print(" ")
        elif computador == 3:
            print("Computador escolheu Tesoura")
            sleep(2)
            print("Vencedor: Computador")
            print(" ")
            ganhacomputador += 1
    elif jogador == 3:
        print("{} escolheu Tesoura".format(nome))
        if computador == 1:
            print("Computador escolheu Pedra")
            sleep(2)
            print("Vencedor: Computador")
            print(" ")
            ganhacomputador += 1
        elif computador == 2:
            print("Computador escolheu Papel")
            sleep(2)
            print("Vencedor: {}".format(nome))
            print()
            ganhajogador += 1
        elif jogador == computador:
            print("Computador escolheu Tesoura")
            sleep(2)
            print("Empate!!")
            print()
    else:
        ganhacomputador += 1
    if ganhajogador == 3 or ganhacomputador == 3:
        print(" ")
        print("[PLACAR FINAL: Jogador {} X {} COMPUTADOR]".format(ganhajogador, ganhacomputador))
    if ganhajogador == 3:
        print(" ")
        print("RECEBA O CAMPEÃO!!!")
        for c in range(3,0,-1):
            sleep(c)
            print(c)
        print("O jogador foi campeão com {} vitórias!!".format(ganhajogador))
        break
    elif ganhacomputador == 3:
        print(" ")
        print('RECEBA O CAMPEÃO!!!')
        for c in range(3,0,-1):
            sleep(c)
            print(c)
        print("O Computador foi campeão com {} vitórias!!".format(ganhacomputador))
        break
print("Comecem os fogos!!!")
for c in range(0,10):
    print("BOOM!! BOOM!! POOWWWW!!!!")
    sleep(1)
print("Até a proxima!!")
sleep(5)
