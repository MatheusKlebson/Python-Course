#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

from time import sleep
times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")
print("="*50)
print("{:^50}".format("DADOS DO BRASILEIRÃO 2019"))
print("="*50)
print(f"Lista de times: {times}")
print("="*50)
print("Os 5 primeiros times: {}".format(times[:5]))
print("="*50)
print("Os 4 primeiros times: {}".format(times[-4:]))
print("="*50)
print("Em ordem alfabetica: {}".format(sorted(times)))
print("="*50)
print("A chapecoense está na {}ª Posição".format(times.index("Chapecoense")+1))
print("="*50)
print("Fim do programa do campeonato brasileiro")
