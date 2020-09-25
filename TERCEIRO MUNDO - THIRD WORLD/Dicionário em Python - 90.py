#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno["Nome"] = str(input("Nome do aluno: ").strip().title())
aluno["Média"] = float(input(f"Média do {aluno['Nome']}: "))
if aluno["Média"] >= 7 and aluno["Média"] <= 10:
    aluno["Situação"] = "APROVADO"
elif aluno["Média"] >= 5 and aluno["Média"] < 7:
    aluno["Situação"] = "RECUPERAÇÃO"
elif aluno["Média"] >= 0 and aluno["Média"] < 5:
    aluno["Situação"] = "REPROVADO"
print("-="*30)
for v, k in aluno.items():
    print(f" - {v} = {k}")

#Outra forma de adicionar no Diciónario
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
aluno = {"Nome":nome,"Media":media,"Situação":situacao}
print("="*50)
for k,v in aluno.items():
    print(f"- {k} é igual a {v}")