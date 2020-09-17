#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
ganhajogador = 0
print("="*30)
print("{:^30}".format("JOGO DO PAR OU IMPAR"))
print("="*30)
print("RECOMENDADO: ESCOLHA UM NÚMERO ENTRE 0 A 10")
while True:
    print("=" * 20)
    print("{:^20}".format("VAMOS JOGAR"))
    print("=" * 20)
    computador = randint(0,10)
    jogador = int(input("Escolha um número: "))
    escolha = str(input("Par ou Impar(P/i): ")).upper().strip()[0]
    while not escolha in "PI":
        escolha = str(input("Digite corretamente. Par ou Impar[P/I]: ")).upper().strip()[0]
    print("Computador jogou: {}".format(computador))
    resultado = computador + jogador
    print(f"Resultado: {resultado}")
    if resultado % 2 == 0:
        print("DEU PAR")
        if escolha == "P":
            ganhajogador += 1
        if escolha == "I":
            break
    else:
        print("DEU IMPAR")
        if escolha == "I":
            ganhajogador += 1
        if escolha == "P":
            break
print("O jogador teve {} Vitorias seguidas".format(ganhajogador))