# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(anoNasc):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    print(f"Com {idade} anos - ",end=" ")


nascimento = int(input("Ano que você nasceu: "))
voto(nascimento)
