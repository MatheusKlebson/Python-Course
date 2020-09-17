#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input("Velocidade do carro em km:"))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print("A multa custa {}R$".format(multa))
else:
    print("Dirija com segurança")
