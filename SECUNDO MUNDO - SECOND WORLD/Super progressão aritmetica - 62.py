#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
# no final mostre quantos termos foram mostrados
print("="*25)
print("PROGRESSÃO ARITMETICA")
print("="*25)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(" {} ->".format(termo),end="")
        termo += razão
        cont += 1
    print(" PAUSA")
    mais = int(input("Quanto temos a mais? "))
print(f"Total de termos: {total} Termos")