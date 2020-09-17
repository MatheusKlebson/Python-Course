#Exercício Python 018: Faça um programa que leia um ângulo qualquer
# mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians,sin,cos,tan
angulo = float(input("Angulo mede:"))
cos = cos(radians(angulo))
print("COSSENO MEDE",cos)
seno = sin(radians(angulo))
print("SENO MEDE",seno)
tangente = tan(radians(angulo))
print("TANGENTE MEDE",tangente)