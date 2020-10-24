# Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)
def readInt(message):
    okay = False
    while True:
        n = str(input(message))
        if n.isnumeric():
            int(n)
            okay = True
            break
        else:
            print("ERROR!! YOU NOT WRITED A NUMBER")
    return n


print("="*50)
number = readInt("WRITE A NUMBER, PLEASE:")
print(f"YOU WRITED THE NUMBER {number}, THANKS A LOT!!")