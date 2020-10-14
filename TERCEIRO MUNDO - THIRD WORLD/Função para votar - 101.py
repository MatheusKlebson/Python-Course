# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(anoNasc):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if idade >= 16 and idade < 18 or idade > 70:
        return f"Com {idade} anos - VOTO: OPCIONAL"
    elif idade >= 18 and idade <= 70:
        return f"Com {idade} anos - VOTO: OBRIGATÓRIO"
    else:
        return f"Com {idade} anos - VOTO: NEGADO"


print("="*50)
nascimento = int(input("Ano que você nasceu: "))
print(voto(nascimento))
