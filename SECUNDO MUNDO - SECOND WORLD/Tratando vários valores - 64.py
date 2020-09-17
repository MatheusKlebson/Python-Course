#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0
numeros = 0
soma = 0
n = int(input("Digite um número: "))
while n != 999:
    numeros += 1
    soma += n
    n = int(input("Digite um número: "))
print(f"A soma entre eles é {soma}")
print(f"O total de números digitados foram {numeros}")