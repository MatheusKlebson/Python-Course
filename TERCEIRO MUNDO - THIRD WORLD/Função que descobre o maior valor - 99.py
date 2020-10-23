# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# mostre os valores recebidos
# total de valores
# e o maior numero entre eles
from random import randint
def fisrtNumber(*numbers):
    print("="*50)
    print(f"Received values: {numbers}")
    print(f"Total values: {len(numbers)}")

fisrtNumber(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
fisrtNumber(randint(0,10),randint(0,10))
fisrtNumber(randint(0,10),randint(0,10),randint(0,10))
fisrtNumber(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
fisrtNumber()
