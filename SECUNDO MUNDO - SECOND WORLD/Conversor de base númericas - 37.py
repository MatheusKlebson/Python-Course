#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input("Número:"))
escolha = int(input('''[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL
DIGITE: '''))
if escolha == 1:
    print("Número {} convertido em Binário: {}".format(n,bin(n)[2:]))
elif escolha == 2:
    print("Número {} convertido em Octal: {}".format(n,oct(n)[2:]))
elif escolha == 3:
    print("Número {} convertido em Hexadecimal: {}".format(n,hex(n)[2:]))
else:
    print("Opção invalida!")
