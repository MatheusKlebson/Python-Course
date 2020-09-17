#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem
# informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
anonasc = int(input("Ano de nascimento: "))
anoatual = date.today().year
idade = anoatual - anonasc
print("O jovem tem {} anos em {}".format(idade,anoatual))
if idade > 18:
    prazo = idade - 18
    anoalis = anoatual - prazo
    print("Passou {} anos do seu alistamento".format(prazo))
    print("Deveria ter se alistado em {}".format(anoalis))
elif idade < 18:
    prazo = 18 - idade
    anoalis = anoatual + prazo
    print("O seu alistamento será daqui a {} anos".format(prazo))
    print("Deverá se alistar em {}".format(anoalis))
elif idade == 18:
    print("Deverá se alistar IMEDIATAMENTE!!")