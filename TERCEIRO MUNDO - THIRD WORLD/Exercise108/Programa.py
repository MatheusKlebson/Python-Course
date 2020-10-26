# Exercício Python 108: Adapte o código do desafio #107, 
# criando uma função adicional chamada moeda() que consiga mostrar os números 
# como um valor monetário formatado.


from Moeda import increase,decrease,double,half
price_product = float(input("HOW MUCH THE PRODUCT COSTS?U$"))
print(f"The double is {moeda(double(price_product))}")
print(f"The half is {moeda(half(price_product))}")
print(f"The increase from 10% is {moeda(increase(price_product,10))}")
