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
print("="*65)
print(jogador)
print("="*65)
for k,v in jogador.items():
    print(f"{k}: {v}")
print("="*65)
print(f"O jogador {jogador['Nome']} jogou {tot} partidas. ")
for i, v in enumerate(jogador["Gols"]):
    print(f" => Na partida {i+1}, fez {v} gols")
print(f"Foi um total de {jogador['Total de gols']} gols")
'''ASSISTI A AULA, SE PRECISO COPIA O CÓDIGO DO GUANABARA E ESTUDA COM CALMA, 
É O ULTIMO EXERCICIO FAZ SENTIDO NÃO TA CONSEGUINDO RESOLVER'''