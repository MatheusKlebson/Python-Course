#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km
# R$0,45 para viagens mais longas.
distancia = float(input("A distancia da viagem em km:"))
if distancia <= 200:
    preço = distancia*0.50
    print("A viagem vai custar: {:.2f}R$".format(preço))
else:
    preço = distancia*0.40
    print("A viagem vai custar: {:.2f}R$".format(preço))
