# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA  
# criar palpites.O programa vai perguntar quantos jogos serão gerados 
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
lista = []
print("="*30)
print("{:^30}".format("PALPITES DA MEGA SENA"))
print("="*30)
totjogos = int(input("Quantos jogos deseja sortear? "))
tot = 0
while tot < totjogos:
    cont = 0
    while True:
        numero = randint(1,60)
        if not numero in lista:
            lista.append(numero)
            cont += 1
        if cont == 6:
            break
    tot += 1
print(lista)