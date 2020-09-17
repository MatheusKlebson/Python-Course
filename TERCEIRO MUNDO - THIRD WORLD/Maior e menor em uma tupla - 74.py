#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados
# também indique o menor e o maior valor que estão na tupla.
from random import randint
print("="*30)
print("{:^30}".format("SORTEANDO 5 ALGARISMOS"))
print("="*30)
numeros = (randint(0,10),randint(0,10),randint(0,10),
           randint(0,10),randint(0,10))
print("Lista de números sorteados: ",end="")
for tabela in numeros:
    print(tabela,end=" ")
for n in range(0,len(numeros)):
    print(f"\n{n + 1}º Número: {numeros[n]}")
print(f"\nO menor número sorteado: {min(numeros)}")
print(f"O maior número sorteado: {max(numeros)}")