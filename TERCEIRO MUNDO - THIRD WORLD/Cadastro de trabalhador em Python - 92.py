# Exercício Python 092: Crie um programa que leia nome, ano de nascimento 
# carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (34 anos de trabalho).
from datetime import date
dados = {}
dados["Nome"] = str(input("Nome do cidadão: ")).strip().title()
AnoNasc = int(input("Ano de Nascimento: "))
AnoAtual = date.today().year
dados["Idade"] = AnoAtual - AnoNasc 
dados["Carteira"] = int(input("Número da carteira de trabalho (0 caso não tenha): "))
if dados["Carteira"] != 0:
    dados["Ano de contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário do funcionário: "))
    AnoAposentadoria = dados["Ano de contratação"] + 34
    IdadeAposentadoria = AnoAposentadoria - AnoNasc
    dados["Aposentadoria"] = IdadeAposentadoria
else:
    print(f"O cidadão {dados['Nome']} está desempregado...")
print(dados)