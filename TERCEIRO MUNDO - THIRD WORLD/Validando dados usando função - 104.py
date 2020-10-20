# Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)
def readInt(message):
    number = str(input(message))
    
number = readInt("Write a number: ")
print(f"You writed a {number}, Thanks!!")
