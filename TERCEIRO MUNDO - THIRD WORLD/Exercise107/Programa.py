# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as 
# funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from Moeda import increase,decrease,double,half
price_product = float(input("HOW MUCH THE PRODUCT COSTS?U$"))
print(f"The double is {double(price_product)}")
print(f"The half is {half(price_product)}")
print(f"The increase from 10% is {increase(price_product,10)}")
