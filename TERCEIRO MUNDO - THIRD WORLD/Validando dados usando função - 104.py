# Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)
def readInt(message):
    okay = False
    while True:
        number = str(input(message))
        if number.isnumeric():
            value = number
            okay = True 
        else:
            print("ERROR!! YOU NOT WRITED A NUMBER")
        if okay == True:
            break
    return value

    
print("=" * 50)
number = readInt("Write a number: ")
print(f"You writed a number {number}, Thanks!!")
