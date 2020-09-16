#Exercício Python 012: Faça um algoritmo que leia o preço de um produto
# mostre seu novo preço, com 5% de desconto.
produto = float(input("Preço do produto:R$"))
novo = produto - (produto*5/100)
print("O novo preço será de",novo,"R$")