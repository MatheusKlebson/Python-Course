#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos 
#cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    num = int(input("Digite um número: "))
    if num not in lista:
        lista.append(num)
    else:
        print("O número já está dentro da lista, não irei adicionar.")
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
lista.sort()
print(f"Lista gerada: {lista}")