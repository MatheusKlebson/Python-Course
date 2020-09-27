# Exercício Python 092: Crie um programa que leia nome, ano de nascimento 
# carteira de trabalho e cadastre-o (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (35 anos de trabalho).
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
    AnoAposentadoria = dados["Ano de contratação"] + 35
    IdadeAposentadoria = AnoAposentadoria - AnoNasc
    dados["Aposentadoria"] = IdadeAposentadoria
    print("="*50)
    print(f''' 
    - NOME: {dados["Nome"]}
    - IDADE: {dados["Idade"]}
    - CTPS: {dados["Carteira"]}
    - Ano de contratação: {dados["Ano de contratação"]}''')
'''if dados["Carteira"] == 0:
    print(f"CTPS: Não possui, o cidadão está desempregado")'''