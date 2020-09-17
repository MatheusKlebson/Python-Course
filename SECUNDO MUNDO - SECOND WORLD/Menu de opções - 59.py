#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
'''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
sleep(2)
print("Escolha o que deseja...")
escolha = 0
while escolha != 5:
    escolha = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Digite: '''))
    sleep(2)
    if escolha == 1:
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}")
    elif escolha == 2:
        multiplica = n1 * n2
        print(f"{n1} X {n2} = {multiplica}")
    elif escolha == 3:
        if n1 > n2:
            print("Primeiro valor é o maior!!")
            print(f"Valor: {n1}")
        else:
            print("Segundo valor é o maior!!")
            print(f"Valor: {n2}")
    elif escolha == 4:
        n1 = int(input("Digite um novo valor(Primeiro valor): "))
        n2 = int(input("Digite um novo valor(Segundo valor): "))
    elif escolha == 5:
        print("Programa chegou ao fim...")
    else:
        print("Valor invalido")
    sleep(2)
print("Volte sempre")