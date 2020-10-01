# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas x
# B) A média de idade x
# C) Uma lista com as mulheres x
# D) Uma lista de pessoas com idade acima da média
dados = []
mulheres = []
pessoa = {}
somaidade = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome da Pessoa: ")).strip().title()
    pessoa["Idade"] = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    while sexo not in "MF":
        print("ERRO!! Escreva M ou F...")
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    if sexo in "MF":
        pessoa["Sexo"] = sexo
    if sexo == "F":
        mulheres.append(pessoa["Nome"])
    somaidade = somaidade + pessoa["Idade"]
    dados.append(pessoa.copy())
     
    media = somaidade/len(dados)
    option = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    while not option in "SN":
        print("ERRO!! Escreva S ou N...")
        option = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if option == "N":
        break
print("="*55)
print(f"Total de pessoas cadastradas: {len(dados)}")
print(f"Média do grupo: {media}")
print(f"Nome das mulheres: {mulheres}")
print("Lista de pessoas acima da media: ")
for tabela in dados:
    if tabela["Idade"] >= media:
        print("   -   ",end="")
        for k,v in tabela.items():
            print(f"{k} = {v}; ",end="") 
        print()
print("<<<< ENCERRADO >>>>")
