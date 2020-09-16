#Exercício Python 004: Faça um programa que leia algo pelo teclado
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input("Digite algo: ")
print("É númerico? ",n.isnumeric())
print("É alfabetico? ",n.isalpha())
print("É alfanúmerico? ",n.isalnum())
print("É Capitalizado? ",n.istitle())
print("É só letras minusculas? ",n.islower())
print("É só letras maiusculas? ",n.isupper())
print("É só espaços? ",n.isspace())