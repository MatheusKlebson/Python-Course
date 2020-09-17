#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# programa vai informar quantas cédulas de cada valor serão entregues.
# OBS:considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5 e R$1.
print("="*30)
print("{:^30}".format("CAIXA ELETRONICO"))
print("="*30)
valor = int(input("Quanto deseja sacar?R$"))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"O total de cedulas de {ced}R$: {totced} Cedulas")
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if ced == 0:
            break
print("Volte sempre!!")