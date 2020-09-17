#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1,5): #Laço de repetição for, que mostra o limite de pessoas
    print("="*30)
    print("{:^30}".format(f"{p}ªPessoa")) #Cabeçalho
    print("="*30)
    peso = float(input("Peso(Kg): ")) #Variavel que recebe o peço de cada pessoa
    # Condição que permita receber o primeiro valor
    if p == 1:
        maior = peso
        menor = peso
    # Condição que permita separar o maior do menor
    else:
        # Condição para receber o maior peso
        if peso > maior:
            maior = peso #Variavel que recebe o maior peso
        # Condição para receber o menor peso
        if peso < menor:
            menor = peso #Variavel que recebe o menor peso
'''Mostrar os valores dos pesos na tela'''
print("O maior peso: {}Kg".format(maior))
print("O menor peso: {}Kg".format(menor))