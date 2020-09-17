#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
maior = 0
menor = 0
for cont in range(0,5):
    lista.append(int(input(f"Número na {cont+1}º Posição: ")))
    if cont == 0:
        maior = lista[cont]
        menor = lista[cont]
    else:
        if maior < lista[cont]:
            maior = lista[cont]
        if menor > lista[cont]:
            menor = lista[cont]
print(f"A lista gerada: {lista}")
print("="*30)
print(f"Maior da lista: {maior}")
print(f"Menor da lista: {menor}")
print("="*30)
for p, v in enumerate(lista):
    if maior == v:
        print(f"Posição do maior: {p+1}º")
    if menor == v:
        print(f"Posição do menor: {p+1}")