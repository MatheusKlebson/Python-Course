import moeda

p = float(input("Preço do produto?R$"))
print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}")
print(f"O aumento de 10%, fica {moeda.aumentar(p,10,True)}")
