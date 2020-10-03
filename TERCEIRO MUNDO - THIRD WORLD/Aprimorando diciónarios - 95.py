# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, x 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
time = list()
partidas = list()
while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do jogador: ")).strip().title()
    tot = int(input(f"Total de partidas que {jogador['Nome']} participou: "))
    for c in range(0,tot):
        partidas.append(int(input(f"Total de gols feito na {c+1}º Partida: ")))
    jogador["Gols"] = partidas[:]
    jogador["Total de gols"] = sum(partidas)
    time.append(jogador.copy())

    option = " "
    while not option in "SN":
        option = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if option == "N":
        break
print("="*30)
print("cod",end="")
for i in jogador.keys():
    print(f"{i:<15}",end="")
print()
print("-"*40)
for k, v in enumerate(time):
    print(f"{k:>3}",end="")
    for d in v.values():
        print(f"{str():<15}",end="")
    print()
print("-"40)
'''ASSISTI A AULA, SE PRECISO COPIA O CÓDIGO DO GUANABARA E ESTUDA COM CALMA, 
É O ULTIMO EXERCICIO FAZ SENTIDO NÃO TA CONSEGUINDO RESOLVER'''