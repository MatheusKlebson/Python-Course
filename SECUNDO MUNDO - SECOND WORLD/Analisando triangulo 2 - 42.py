#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- Triângulo Isósceles. Tem dois lados iguais e um diferente.
#Triângulo Escaleno. Nenhum dos lados é igual.
r1 = float(input("Primeira reta:"))
r2 = float(input("Segunda reta:"))
r3 = float(input("Terceira reta:"))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("E triangulo!!")
    if r1 == r2 == r3:
        print("EQUILATERO: Todos os lados são iguais")
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print("Isósceles. Tem dois lados iguais e um diferente")
    elif r1 != r2 and r2 != r3:
        print("Escaleno. Nenhum dos lados é igual.")
else:
    print("Nao é triangulo!!")