#   Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
#   guarde tudo em uma lista composta. 
#   No final, mostre um boletim contendo a média de cada um 
#   permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
while True:
    nome = str(input("Digite o nome do aluno: ")).strip().title()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digute a segunda nota: "))
    media = (nota1 + nota2)/2
    lista.append(nome)
    lista.append(nota1,nota2)
    lista.append(media)

    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break

print(lista)