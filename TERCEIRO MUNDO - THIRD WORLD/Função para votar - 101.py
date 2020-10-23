# Exercício Python 101: Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro 
# ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def vote(born_year):
    from datetime import date
    currentYear = date.today().year
    age = currentYear - born_year 
    print(f"The person have {age}, situation: ",end="")
    if age >= 18 and age < 65:
        return "Obrigatory"
    elif age >= 16 and age < 18 or age >= 65:
        return "Optional"
    else:
        return "Denied"


print("="*50)
bornYear = int(input("What is your year of birth? "))
print(vote(bornYear))