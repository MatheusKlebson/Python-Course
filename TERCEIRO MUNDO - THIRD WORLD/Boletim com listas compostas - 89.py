#   Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
#   guarde tudo em uma lista composta. 
#   No final, mostre um boletim contendo a média de cada um 
#   permita que o usuário possa mostrar as notas de cada aluno individualmente.

nome = str(input("Digite o nome do aluno: ")).strip().title()
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digute a segunda nota: "))
media = (nota1 + nota2)/2
print([nome,[nota1,nota2],media])