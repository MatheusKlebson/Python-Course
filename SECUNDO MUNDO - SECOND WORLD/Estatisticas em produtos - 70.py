#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.x
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:x
#A) qual é o total gasto na compra. x
#B) quantos produtos custam mais de R$1000. x
#C) qual é o nome do produto mais barato.
custo = 0
maior1000 = 0
nomebarato = " "
valorbarato = 0
totalproduto = 0
print("="*30)
print("{:^30}".format("MERCADO SANTOS ARAUJO"))
while True:
    print("=" * 30)
    nome = str(input("Nome do produto: ")).strip().title()
    preço = float(input("Preço:R$"))
    print("="*30)
    custo += preço
    totalproduto += 1
    if preço >= 1000:
        maior1000 += 1
    if totalproduto == 1:
        nomebarato = nome
        valorbarato = preço
    else:
        if preço < valorbarato:
            valorbarato = preço
            nomebarato = nome
    resposta = " "
    while not resposta in "SN":
        resposta = str(input("Quer continuar?[S/N]:")).upper().strip()[0]
    if resposta == "N":
        break
print("Valor total das compras:R${:.2f}".format(custo))
print(f"Total de Produtos que custam acima de 1000R$: {maior1000}")
print("O nome do produto mais barato é {} que custa {:.2f}R$".format(nomebarato,valorbarato))