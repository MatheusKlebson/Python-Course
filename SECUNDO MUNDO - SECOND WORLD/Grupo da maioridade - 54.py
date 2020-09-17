#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
anoatual = date.today().year
maior = menor = 0
for p in range(1,8):
    ano = int(input(f"Em que ano a {p}ª Pessoa nasceu: "))
    idade = anoatual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("Maiores de idade: {} Pessoas".format(maior))
print("Menores de idade: {} Pessoas".format(menor))