# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def mostraLinha(txt):
    print("=" * 50)
    print("{:^50}".format(txt))
    print("=" * 50)
def area(largura,comprimento):
    area = largura * comprimento
    print(f"A dimensão da area {largura}X{comprimento} é de {area}m2")


mostraLinha("CUMPRIMENTO DA ÁREA")
l = float(input("Largura: "))
c = float(input("Cumprimento: "))
area(l,c)