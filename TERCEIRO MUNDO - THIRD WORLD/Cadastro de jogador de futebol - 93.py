# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
jogador["Nome"] = str(input("Nome do jogador: ").strip().title())
partidas = int(input("Total de partidas jogadas: "))
for jogos in range(0,partidas):
    gols.append(int(input(f"Total de gols feitos na {jogos}º Partida: ")))
print(gols)