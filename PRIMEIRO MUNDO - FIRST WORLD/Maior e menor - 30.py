#Exercício Python 033: Faça um programa que leia três números
# mostre qual é o maior e qual é o menor.
n1 = int(input("Primeiro número:"))
n2 = int(input("Segundo número:"))
n3 = int(input("Terceiro número:"))
if n1 > n2 > n3:
    print("Maior: {}".format(n1))
    print("Menor: {}".format(n3))
elif n2 > n1 > n3:
    print("Maior: {}".format(n2))
    print("Menor: {}".format(n3))
elif n3 > n2 > n1:
    print("Maior: {}".format(n3))
    print("Menor: {}".format(n1))
elif n3 > n1 > n2:
    print("Maior: {}".format(n3))
    print("Menor: {}".format(n2))
elif n2 > n1 > n3:
    print("Maior: {}".format(n2))
    print("Menor: {}".format(n3))
elif n2 > n3 > n1:
    print("Maior: {}".format(n2))
    print("Menor: {}".format(n3))