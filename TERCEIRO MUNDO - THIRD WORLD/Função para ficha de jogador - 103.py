# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: o nome de um jogador 
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(jogador="<desconhecido>",gols=0):
    print(f"O jogador {jogador} fez {gols} gols no campeonato")


print("="*50)
nome = str(input("Nome do jogador: ").strip().title())
gol = str(input(f"Total de gols: ")).strip()
if gol == '':
    gol = 0
if nome == '':
    nome = "<desconhecido>"
ficha(nome,gol)