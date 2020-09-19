#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso:
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
impares = []
pares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
print(f"Lista: {lista}")
print(f"Lista dos pares: {pares}")
print(f"Lista dos ímpares: {impares}")