#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
totdivisivel = 0
naodivisivel = 0
num = int(input("Número: "))
for c in range(1,num + 1):
    if num % c == 0: # É divisivel, amarelo
        print("\033[33m{} ".format(c), end="")
        totdivisivel += 1
    else: # Não é divisivel, roxo
        print("\033[35m{} ".format(c),end="")
        naodivisivel += 1
#Branco para divisivel e não divisivel
print(f"\n\033[30mNão divisivel(Roxo): {naodivisivel} ")
print(f"Divisivel(Amarelo): {totdivisivel} ")
if totdivisivel == 2: #Azul quando for primo
    print("\033[34mO número {} é PRIMO!!".format(num))
else: #Vermelho quando não for primo
    print("\033[31mO número {} NÃO É PRIMO!!".format(num))