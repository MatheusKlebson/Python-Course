#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
while True:
    try:
        ano = int(input("Digite um ano[Digite 0 para saber o ano atual]:"))
        if ano == 0:
            ano = date.today().year
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print("O ano {} é BISSEXTO!!".format(ano))
        else:
            print("O ano {} NÃO É BISSEXTO!!".format(ano))
    except:
        print("Voce digitou um string!! \nPrograma fechado!")
        break