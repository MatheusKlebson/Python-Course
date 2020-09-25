#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
nome = str(input("Digite o nome do aluno: ")).strip().title()
media = float(input(f"Média do {nome}: "))
if media >= 7 and media <= 10:
    situacao = "APROVADO"
elif media > 4.9 and media < 7:
    situacao = "RECUPERAÇÃO"
elif media >= 0 and media < 5:
    situacao = "REPROVADO"
else:
    print("O aluno possui uma média inválida...")
aluno = {"Nome":nome,"Media":media,"situação":situacao}
print(aluno)