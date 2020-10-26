from moeda import aumentar,dobro,metade,diminuir

p = float(input("Quanto custa?R$"))
print(f"O dobro é R${dobro(p)}")
print(f"A metade é R${metade(p)}")
print(f"Com aumento de 10% fica R${aumentar(p,10)}")