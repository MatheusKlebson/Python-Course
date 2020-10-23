# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# mostre os valores recebidos
# total de valores
# e o maior numero entre eles
from random import randint
def fisrtNumber(*num):
    print("="*50)
    print(f"Received values: {num}")


fisrtNumber(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
fisrtNumber(randint(0,10),randint(0,10))
fisrtNumber(randint(0,10),randint(0,10),randint(0,10))
fisrtNumber(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
fisrtNumber()
