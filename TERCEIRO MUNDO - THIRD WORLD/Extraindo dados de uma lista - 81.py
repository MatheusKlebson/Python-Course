#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.         
# Depois disso, mostre:                                          
# A) Quantos números foram digitados.                            
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.
totnum = 0
lista = []
print("="*30)
print("{:^30}".format('Digitando e guardando números'))
print("="*30)
while True:
  num = int(input("Digite um número: "))
  totnum += 1
  lista.append(num)
  
  opção = " "
  while not opção in "SN":
    opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
  if opção == "N":
    break
print("="*30)
print("{:^30}".format('FIM DO PRGRAMA'))
print("="*30)
print(f"Total de números digitados na lista: {totnum}")
print("="*30)
lista.sort(reverse=True); print(f"Lista em ordem descrecente: {lista}")
print("="*30)
if 5 in lista:
  print("O número 5 faz parte da lista!!")
  print("Foi encontrado nos lugar(es): ",end="")
  for p,v in enumerate(lista):
    if v == 5:
      print(f"[{p+1}]",end="")
else:
  print("O número 5 não está na lista!")