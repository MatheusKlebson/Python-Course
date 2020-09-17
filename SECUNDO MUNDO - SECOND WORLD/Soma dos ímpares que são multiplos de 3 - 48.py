#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# que se encontram no intervalo de 1 até 500.
total = 0
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        #print(c)
        total += 1 #guardando numa unica variavel cada numero que seja divisivel de 3
        soma += c #Somando os impares multiplos por 3
print("O total de Impares é {}".format(total))
print(f"A soma entre todos os Impares: {soma}")