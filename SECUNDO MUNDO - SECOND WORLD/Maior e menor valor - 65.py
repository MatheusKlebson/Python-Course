#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. x
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. x

r = "S"
media = 0
somanum = 0
quantnum = 0
maior = 0
menor = 0
while r == "S":
    n = int(input("Número: "))
    r = str(input("Deseja continuar?[S/N]: ")).strip().upper()[0]
    if not r in "SN":
        r = str(input("Digite corretamente. Deseja continuar?[S/N]: ")).strip().upper()[0]
    quantnum += 1
    somanum += n
    if quantnum == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = somanum/quantnum
print(f"A média é {media}")
print("Maior número digitado: {}".format(maior))
print("Menor número digitado: {}".format(menor))