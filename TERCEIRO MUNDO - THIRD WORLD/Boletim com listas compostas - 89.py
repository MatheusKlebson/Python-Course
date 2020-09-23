#   Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
#   guarde tudo em uma lista composta. 
#   No final, mostre um boletim contendo a média de cada um 
#   permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
while True:
    nome = str(input("Digite o nome do aluno: ")).strip().title()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2)/2
    lista.append([nome,[nota1,nota2],media])
    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
print("="*30)
print(f"{'NUM':^5}{'NOME':>10}{'MÉDIA':>12}")
print("="*30)
for indice, aluno in enumerate(lista):
    print(f"{indice:^5}{aluno[0]:>11}{aluno[2]:>10}")
print("="*30)
while True:
    opc = int(input('''Coloque a númeração do aluno que você deseja ver as notas,
(999 termina o programa) Digite: '''))
    if opc < len(lista):
        print(f"A notas do aluno {aluno[opc][0]} são: {aluno[opc][1]}")
    if opc == 999:
        break
    else:
        print("Aluno digitado não existe")