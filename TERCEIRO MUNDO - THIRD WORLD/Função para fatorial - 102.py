#  Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#  o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#  indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(calcular,show):
    if show == True:
        f = 1
        for c in range(calcular,0,-1):
            f *= c
        return f
    else;
        f = 1
        for c in range(calcular,0,-1):
            f *= c
        return f
num = int(input("Digite um número para o fatorial: "))
print(fatorial(num,show=True))
