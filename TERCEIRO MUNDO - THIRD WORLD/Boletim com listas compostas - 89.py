#   Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
#   guarde tudo em uma lista composta. 
#   No final, mostre um boletim contendo a média de cada um 
#   permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = [[],[],[]]
while True:
    lista[0].append(str(input("Digite o nome do aluno: ")).strip().title())
    lista[1].append(float(input("Digite a primeira nota: ")))
    lista[1].append(float(input("Digute a segunda nota: ")))
    lista[2].append((lista[1][0] + lista[1][1]/2))
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break

print(lista)