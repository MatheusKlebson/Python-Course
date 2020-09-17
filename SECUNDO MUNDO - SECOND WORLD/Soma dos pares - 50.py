#Exercício Python 050: Desenvolva um programa que leia seis números inteiros
# mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
totpar = 0
soma = 0
for c in range(0,6):
    n = int(input("Digite um número:"))
    if n % 2 == 0:
        totpar += 1
        soma += n
print("Total de pares digitados: {}".format(totpar))
print("A soma entre os pares: {}".format(soma))