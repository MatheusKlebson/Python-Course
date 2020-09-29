#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média
dados = []
pessoa = {}
while True:
    pessoa["Nome"] = str(input("Nome da Pessoa: ")).strip().title()
    pessoa["Idade"] = int(input("Idade: "))
    pessoa["Sexo"] = str(input("Sexo: [M/F]")).strip().upper()[0]
    dados.append(pessoa.copy())
    option = " "
    while not option in "SN":
        option = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if option == "N":
        break
print(dados)
