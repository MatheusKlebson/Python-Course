# Exercício Python 100: Faça um programa que tenha uma lista chamada números 
# duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números 
# vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
def sorteia():
    for cont in range(0,5):
        num = randint(1,10)
        numeros.append(num)
    

def somaPar():
    soma = 0
    for cont in range(0,5):
        if numeros[cont] % 2 == 0:
            soma += numeros[cont]
    print(f"Somando os pares da lista {numeros} o resultado é: {soma}")


from random import randint
numeros = []
sorteia()
print(f"Valores sorteados: {numeros}")
somaPar()
