# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, x 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
while True:
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
    jogadores.append(jogador.copy())

    option = " "
    while not option in "SN":
        option = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if option == "N":
        break
print(jogadores)
'''Discionario jogador, Estrutura: {'Nome': 'Matheus', 'Gols': [0, 4, 8, 6, 3], 'Total de Gols': 21}'''
'''[{'Nome': 'Matheus', 'Gols': [0, 3], 'Total de Gols': 3}, {'Nome': 'Micaias', 'Gols': [2, 0, 1], 'Total de Gols': 3}]'''
print("="*65)
print("{:^65}".format("DADOS DOS JOGADORES"))
print("="*65)
print(f"{'NUM':>5}{'NOME':>15}{'GOLS':>20}{'TOTAL DE GOLS':>23}")
print('-'*65)

    
