# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, x 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
partidas = list()
jogador["Nome"] = str(input("Nome do jogador: ")).strip().title()
tot = int(input(f"Total de partidas que {jogador['Nome']} participou: "))
for c in range(1,tot + 1):
    partidas.append(int(input(f"Total de gols feito na {c}º Partida: ")))
jogador["Gols"] = partidas[:]
jogador["Total de gols"] = sum(partidas)
print("="*65)
print(jogador)
print("="*65)
for k,v in jogador.items():
    print(f"{k}: {v}")
print("="*65)
print(f"O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} de partidas. ")
'''ASSISTI A AULA, SE PRECISO COPIA O CÓDIGO DO GUANABARA E ESTUDA COM CALMA, 
É O ULTIMO EXERCICIO FAZ SENTIDO NÃO TA CONSEGUINDO RESOLVER'''