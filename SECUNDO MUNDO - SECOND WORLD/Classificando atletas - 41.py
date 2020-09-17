#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM Até 14 anos: INFANIIL Até 19 amps: JUNIOR Até 25 anos: SENIOR Acima: MASTER
from datetime import date
print("="*23)
print("CLASSIFICANDO ATLETAS")
print("="*23)
ano = int(input("Ano de nascimento do atleta:"))
anoatual = date.today().year
idade = anoatual - ano
print("IDADE DO ATLETA: {} Anos".format(idade))
if idade >= 0 and idade <= 9:
    print("CLASSIFICAÇÃO MIRIM")
elif idade <= 14:
    print("CLASSIFICAÇÃO INFANTIL")
elif idade <= 19:
    print("CLASSIFICAÇÃO JUNIOR")
elif idade <= 25:
    print("CLASSIFICAÇÃO SENIOR")
elif idade > 25:
    print("CLASSIFICAÇÃO MASTER")
else:
    print("IDADE FALSA!!")