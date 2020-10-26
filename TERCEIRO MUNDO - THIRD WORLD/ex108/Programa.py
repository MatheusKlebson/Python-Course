# Exercício Python 108: Adapte o código do desafio #107, 
# criando uma função adicional chamada moeda() que consiga mostrar os números 
# como um valor monetário formatado.
from ex108 import moeda

price_product = float(input("HOW MUCH THE PRODUCT COSTS?U$"))
print(f"A metade de {moeda.moeda(price_product)} é {moeda.moeda(moeda.metade(price_product))}")

