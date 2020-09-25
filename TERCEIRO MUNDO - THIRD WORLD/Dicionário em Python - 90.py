#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno["Nome"] = str(input("Nome do aluno: ").strip().title())
aluno["Média"] = float(input(f"Média do {aluno['Nome']}: "))
