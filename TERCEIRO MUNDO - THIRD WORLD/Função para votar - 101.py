# Exercício Python 101: Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro 
# ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def vote(born_year):
    from datetime import date
    currentYear = date.today().year
    age = currentYear - born_year 
    print(age)


print("="*50)
bornYear = int(input("What is your year of birth? "))
vote(bornYear)