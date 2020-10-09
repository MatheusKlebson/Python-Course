# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
def maior(* num):
    print("="*55)
    print(f"Os valores recebido: {num}")
    print(f"Total de valores recebidos: {len(num)}")
    if len(num) == 0:
        print("O maior valor: 0")
    else:
        print(f"O maior valor: {max(num)}")


maior(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
maior(randint(0,10),randint(0,10))
maior(randint(0,10),randint(0,10),randint(0,10))
maior(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
maior()