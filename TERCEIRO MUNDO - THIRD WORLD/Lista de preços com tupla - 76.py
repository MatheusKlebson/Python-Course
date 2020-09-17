#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
# seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ("COMPUTADOR",1220,
            "TABLET",355,
            "CELULAR",420,
            "GELADEIRA",380,
            "FONE DE OUVIDO",40,
            "CAIXA DE SOM",50)
print("="*50)
print("{:^50}".format("PRODUTOS E PREÇOS"))
print("="*50)
for tabela in range(0,len(produtos)):
    if tabela % 2 == 0:
        print(f"{produtos[tabela]:.<40}",end="")
    else:
        print(f"R${produtos[tabela]:>8.2f}")
print("="*50)