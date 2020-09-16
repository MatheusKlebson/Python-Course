#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura*altura
print("A parede mede uma area de",area)
tinta = area/2
print("Vai ser preciso",tinta,"L de tinta para pintar a parede")