#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Km percorridos: "))
dias = int(input("Quantos dias vai alugar? "))
preço = (dias*60) + (km*0.15)
print("Total a pagar é",preço,"R$")