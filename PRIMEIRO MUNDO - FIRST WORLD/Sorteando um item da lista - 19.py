#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
números =(str(input("Primeiro aluno: ")),
          str(input("Segundo aluno: ")),
          str(input("Terceiro aluno: ")),
          str(input("Quarto aluno: "))
lista = [numeros[0],numeros[1],numeros[2],numeros[3]]
escolhido = choice(lista)
print("O escolhido foi",escolhido)
