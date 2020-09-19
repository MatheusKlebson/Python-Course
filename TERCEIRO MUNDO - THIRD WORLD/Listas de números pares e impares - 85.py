# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos 
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[],[]]
for cont in range(1,8):
    num = int(input(f"Digite o {cont}º valor: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f"Lista dos pares: {sorted(lista[0])}")
print("="*30)
print(f"Lista dos ímpares: {sorted(lista[1])}")