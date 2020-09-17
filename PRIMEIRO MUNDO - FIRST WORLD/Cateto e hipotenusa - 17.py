#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input("Cateto oposto:"))
ca = float(input("Cateto adjacente:"))
hi = hypot(co,ca)
print(hi)