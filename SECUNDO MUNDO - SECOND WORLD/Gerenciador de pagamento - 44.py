#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
from time import sleep
print("="*30)
print("{:^30}".format("MERCADO SANTOS ARAUJO"))
print("="*30)
produto = float(input("Preço do produto:R$"))
opção = int(input('''[1]A vista dinheiro/cheque: 10% de desconto
[2]A vista no cartão: 5% de desconto
[3]Em até 2x no cartão: preço normal
[4]3x ou mais no cartão: 20% de juros
DIGITE: '''))
print("Calculando...")
sleep(2)
print("Valor do produto:{:.2f}R$".format(produto))
if opção == 1:
    total = produto - (produto*10/100)
    print("Desconto: 10%")
    print(f"Total a pagar: {total:.2f}R$")
elif opção == 2:
    total = produto - (produto*5/100)
    print("Desconto: 5%")
    print(f"Total a pagar: {total:.2f}R$")
elif opção == 3:
    print("Parcela: 2x")
    parcela = produto/2
    print("Total a pagar em cada prestação: {:.2f}".format(parcela))
elif opção == 4:
    print("Juros: 20%")
    total = produto + (produto*20/100)
    print(f"Valor do produto com juros: {total:.2f}R$")
    totparcela = int(input("Total de parcelas: "))
    print("Parcela: {}".format(totparcela))
    parcela = total/totparcela
    print(f"Total a pagar em cada prestação:{parcela:.2f}R$")
else:
    print("O programa deu erro!! Opção invalida.")