#Exercício Python 008: Escreva um programa que leia um valor em metros
# exiba convertido em centímetros e milímetros.
#km hm dam m dm cm mm
m = float(input("Distancia em metros: "))
print("Km =",m/1000)
print("hm =",m/100)
print("Dam =",m/10)
print("M =",m)
print("Dm =",m*10)
print("Cm =",m*100)
print("Mm =",m*1000)