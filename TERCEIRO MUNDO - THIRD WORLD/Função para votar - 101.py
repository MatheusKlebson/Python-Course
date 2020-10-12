# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date
def voto(anoNasc):
    idade = date.today().year - anoNasc
    print(f"Com {idade} anos - ",end="")
    if idade >= 18 and idade < 70:
        print("VOTO: OBRIGATÓRIO")
    elif idade >= 16 and idade < 18 or idade >= 70:
        print("VOTO: OPCIONAL")
    else:
        print("VOTO: NEGADO")


print("="*50)
ano = int(input("Em que ano você nasceu: "))
voto(ano)
