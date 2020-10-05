# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def mostraLinha(txt):
    print("=" * 50)
    print(txt)
    print("=" * 50)
def area(largura,comprimento):
    area = (largura * comprimento)/2
    print(f"A dimensão da area {largura}X{comprimento} é de {area}m2")
mostraLinha("CUMPRIMENTO")

