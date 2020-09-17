#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.x
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.x
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
total = 0
soma = 0
while True:
    n = int(input("Número(digite 999 para parar): "))
    if n == 999:
        break
    total += 1
    soma += n
print("Total de números digitados: {}".format(total))
print("A soma dos números digitados: {}".format(soma))