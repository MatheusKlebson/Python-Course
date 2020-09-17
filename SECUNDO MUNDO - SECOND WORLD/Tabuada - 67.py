#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input("Digite um número: "))
    if n < 0:
        break
    for num in range(1,11):
        print("{} X {} = {}".format(n,num,n*num))
print("FIM DA TABUADA")