# Exercício Python 092: Crie um programa que leia nome, ano de nascimento 
# carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = {}
dados["Nome"] = str(input("Nome do cidadão: ")).strip().title()
AnoNasc = int(input("Ano de Nascimento: "))
AnoAtual = date.today().year
dados["Idade"] = AnoNasc - AnoAtual
dados["Carteira"] = int(input("Número da carteira de trabalho (0 caso não tenha): "))
print(dados)