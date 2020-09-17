#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista
valores = list()
print("="*60)
print("{:^60}".format("CRIE UMA LISTA DE NÚMEROS"))
print("="*60)
totnum = int(input("Digite a quantidade de números que estaŕa na lista: "))
print("="*30)
print("{:^30}".format("FIQUE A VONTADE"))
print("="*30)
for cont in range(0,totnum):
  valores.append(int(input(f"Valor na posição {cont+1}: ")))
print("="*45)
print("{:^45}".format(f"LISTA DE {totnum} NÚMEROS FOI FORMADA : {valores}"))
print("="*45)
maior = max(valores)
menor = min(valores)
print(f"Maior valor: {maior}")
print(f"Localização do maior valor: ",end="")
for p, v in enumerate(valores):
  if v == maior:
    print(f"[{p+1}]",end="")
print()
print("="*45)
print(f"Menor valor: {menor}")
print(f"Localização do menor valor: ",end="")
for p, v in enumerate(valores):
  if v == menor:
    print(f"[{p+1}]",end="")

