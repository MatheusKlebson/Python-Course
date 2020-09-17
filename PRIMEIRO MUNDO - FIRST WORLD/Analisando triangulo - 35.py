#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas
# diga ao usuário se elas podem ou não formar um triângulo.
#DICA: Soma os 2 menores, se o resultado for maior que o terceiro lado então da pra formar um triangulo!!!
r1 = float(input("Primeira reta:"))
r2 = float(input("Segunda reta:"))
r3 = float(input("Terceira reta:"))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("E triangulo!!")
else:
    print("Nao é triangulo!!")