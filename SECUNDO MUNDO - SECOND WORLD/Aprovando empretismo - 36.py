#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
casa = float(input("Valor da casa:R$"))
salario = float(input("Salário:R$"))
anos = int(input("Deseja pagar em quantos anos? "))
prestação = casa / (anos * 12)
trinta = salario * 30 / 100
print("Analisando...")
sleep(2)
print(f"30% do salário: {trinta}")
print("Valor de cada prestação: {:.2f}R$".format(prestação))
print("Anos de financiamento: {} anos".format(anos))
if prestação <= trinta:
    print("APROVADO!!")
else:
    print("REPROVADO!!")