import moeda

p = float(input("Preço do produto?R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}")
print(f"O aumento de 10%, fica {moeda.aumentar(p, 10)}")
