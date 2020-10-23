#  Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#  o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#  indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def factorial(calculation,show):
    print("="*50)
    f = 1
    for counter in (calculation,0,-1):
        if show == True:
            print(f"{counter}",end="")
            if counter > 1:
                print(" X ",end="")
            else:
                print(" = ",end="")
        f *= counter
    return f


print("="*50)
nuumber = int(input("Write a number to calculate the factorial: "))
