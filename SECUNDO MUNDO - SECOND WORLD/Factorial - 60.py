#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
from time import sleep
from math import factorial
num = int(input("Número: "))
cont = num
f = factorial(num)
print("Calculando factorial...")
sleep(2)
while cont > 0:
    print(" {} ".format(cont),end="")
    if cont > 1:
        print(" X ",end="")
    else:
        print(" = ",end="")
    cont -= 1
print(" {} ".format(f))