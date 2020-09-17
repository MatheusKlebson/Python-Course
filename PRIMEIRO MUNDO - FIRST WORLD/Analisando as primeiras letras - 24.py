#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input("Nome de uma cidade:")).upper().strip()
print("O primeiro nome é Santo? ",cidade[:5] == "SANTO")
