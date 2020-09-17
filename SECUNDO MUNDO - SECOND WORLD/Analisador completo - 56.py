#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, x
# qual é o nome do homem mais velho
# quantas mulheres têm menos de 20 anos.
somaidade = 0
nomevelho = " "
idadevelho = 0
mulhertot20 = 0
for p in range(1,5):
    print(f"===={p}ªPessoa====") #Cabeçalho do registro
    nome = str(input("Nome: ")).strip() #Nome da pessoa
    idade = int(input("Idade: ")) #Idade da pessoa
    sexo = " " #Variavel para melhorar a usabilidade do usuario
    while not sexo in "MF": #Whle para caso o usuario digitar o sexo errado
        sexo = str(input("Sexo[M/F]:")).strip().upper()[0] #lendo o sexo
    somaidade += idade #Variavel que soma a idade de todos os registrados
    if p == 1 and sexo == "M": #Contador para calcular o homem mais velho
        nomevelho = nome
        idadevelho = idade
    else:
        if idade > idadevelho and sexo == "M": #Condição para saber qual é o mais velho
            nomevelho = nome
            idadevelho = idade
    if sexo == "F" and idade < 20:
        mulhertot20 += 1 #Variavel que recebe o total de mulheres abaixo de 20 anos
mediaidade = somaidade/4 #Media de idade do grupo
print(f"Media de idade do grupo: {mediaidade}") #mostrar a media no terminal
print(f"Nome do homem mais velho é {nomevelho}, sua idade é de {idadevelho} anos") #Mostrar no terminal o nome do homem mais velho e sua idade
print(f"Total de mulheres abaixo de 20 anos: {mulhertot20}") #Mostrar na tela o total de mulheres abaixo de 20 anos