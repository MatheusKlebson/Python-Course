# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(* num):
    print("="*55)
    print(f"Os valores recebido: {num}")


maior(6,8,3,1,6,7,10)
maior(2,4,5,3,1)
maior(5,3,1)
maior()