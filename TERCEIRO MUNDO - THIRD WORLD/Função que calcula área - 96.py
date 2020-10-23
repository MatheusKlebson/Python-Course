# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura,comprimento):
    a = largura * comprimento
    print(f"A area que mede uma dimensão de {largura}x{comprimento} é de {a}m2 ")

larg = float(input("Largura (m): "))
com = float(input("Comprimento (m): "))
area(larg,com)