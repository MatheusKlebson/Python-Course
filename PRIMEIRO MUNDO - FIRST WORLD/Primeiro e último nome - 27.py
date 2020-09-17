#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input("Nome completo: ")).upper().strip()
n = nome.split()
print("O primeiro nome é {}".format(n[0]))
print("O ultimo nome é {}".format(n[(len(n)-1)]))
