# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.
jogador = {}
gol = []
totgol = 0
jogador["Nome"] = str(input("Nome do jogador: ").strip().title())
partidas = int(input(f"Total de partidas que {jogador['Nome']} jogou: "))
for jogos in range(1,partidas + 1):
    golPartida = int(input(f"Total de gols feitos na {jogos}º Partida: "))
    gol.append(golPartida)
    totgol += golPartida
jogador["Gols"] = gol
jogador["Total de Gols"] = totgol
print(jogador)
'''Discionario jogador: {'Nome': 'Matheus', 'Gols': [0, 4, 8, 6, 3], 'Total de Gols': 21}'''
print("="*50)
print("{:^50}".format("DADOS DO JOGADOR"))
print("="*50)
for k,v in jogador.items():
    print(f"{k} = {v}")
print("-="*25)
print(f"{jogador['Nome']} jogou {partidas} partidas")
for indice,gols in enumerate(gol):
    print(f"Total de gols na {indice + 1}º partida: {gols}")
    