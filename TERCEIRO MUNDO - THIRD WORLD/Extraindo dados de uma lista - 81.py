#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.         
# Depois disso, mostre:                                          
# A) Quantos números foram digitados.                            
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
totnum = 0
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    totnum += 1
    
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
print(f"Lista gerada: {lista}")
print(f"Total de números: {totnum}")
lista.sort(reverse=True)
print(f"Lista descrecente: {lista}")
if 5 in lista:
    print("O número 5 está na lista!!")
else:
    print("O 5 não está na lista")