# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area (width, length):
    a = width * length
    print(f"The area that measures a dimension of {width}x{length} is {a} m2")


def title(text):
    size = len(text) + 4
    print("="*size)
    print(f"  {text}")
    print("="*size)


title("AREA CALCULATION")
larg = float(input("Width (m):"))
com = float(input("Length (m):"))
area(larg, com)