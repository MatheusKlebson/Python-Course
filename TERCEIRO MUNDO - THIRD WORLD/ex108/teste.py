import moeda

p = float(input("Preço do produto?R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"O aumento de 10%, fica {moeda.moeda(moeda.aumentar(p,10))}")
