# Exercício Python 100: Faça um programa que tenha uma lista chamada números 
# duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números 
# vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.
def randomNumbers():
    from random import randint
    for cont in range(0,5):
        num = randint(1,10)
        numbers.append(num)


def sumPairs():
    soma = 0
    for cont in range(0,5):
        if numbers[cont] % 2 == 0:
            soma += numbers[cont]
    print(f"Numbers drawn: {numbers}")
    print(f"Sum Pairs: {soma}")

    
numbers = []
randomNumbers()
sumPairs()
