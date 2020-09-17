#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
# - primeiro valor maior
# - Segundo valor maior
# - ambos são iguais
n1 = int(input("Primeiro valor:"))
n2 = int(input("Segundo valor:"))
if n1 > n2:
    print("O primeiro valor é maior!")
elif n2 > n1:
    print("O segundo valor é maior!")
else:
    print("Ambos são iguais!")
