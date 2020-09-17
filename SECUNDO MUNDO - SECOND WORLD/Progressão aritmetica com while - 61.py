#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
print("="*25)
print("PROGRESSÃO ARITMETICA")
print("="*25)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
termo = primeiro
cont = 1
while cont <= 10:
    print(" {} ->".format(termo),end="")
    termo += razão
    cont += 1
print(" ACABOU")