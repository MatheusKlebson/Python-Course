# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: o nome de um jogador 
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.
def passbook(playerName='<unknown>',goals=0): '''passbook = caderneta'''



def write(text):
    size = len(text) + 4
    print("="*size)
    print(f"  {text}")
    print("="*size)

write("PLAYER DATA")
name = str(input('WRITE THE NAME OF THE PLAYER: '))
totgoal = str(input("WRITE THE TOTAL OF GOALS: "))
passbook(name,totgoal)