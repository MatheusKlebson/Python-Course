#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado
# mostre na tela a sua porção Inteira.
from math import trunc
num = float(input("Número decimal:"))
print(trunc(num))