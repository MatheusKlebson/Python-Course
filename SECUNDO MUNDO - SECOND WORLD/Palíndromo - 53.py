#Exercício Python 053: Crie um programa que leia uma frase qualquer
# diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input("Frase: ")).strip().upper()
separado = frase.split()
junto = "".join(separado)
inverno = junto[::-1]
print("O inverso da frase {} é {}".format(junto,inverno))
if junto == inverno:
    print("É PALINDROMO")
else:
    print("NÃO É PALINDROMO")