#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao total (sem considerar espaços).
#- Quantas letras tem o primeiro nome
from time import sleep
nome = str(input("Nome completo: ")).strip()
n = nome.split()
print("Analisando nome...")
sleep(2)
print("Nome só com letras maiúsculas:",nome.upper())
print("Nome só com letras minúsculas:",nome.lower())
print("Ao todo tem",len(nome) - nome.count(" "),"Letras")
print("O primeiro nome é",n[0],"E possui apenas",nome.find(" "),"Letras")