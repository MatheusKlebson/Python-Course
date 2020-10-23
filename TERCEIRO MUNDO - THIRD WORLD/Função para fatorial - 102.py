#  Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#  o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#  indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def factorial(n,show):
    print("="*50)
    f = 1
    for cont in range(n,0,-1):
        if show == True:
            print(f"{cont}",end="")
            if cont > 1:
                print(" X ",end="")
            else:
                print(" = ",end="")
        f *= cont
    return f


print("="*50)
num = int(input("Digite um número para o fatorial: "))
show = " "
while show not in "SN":
    show = str(input("MOSTRA FATORIAL[S/N]: ")).upper().strip()[0]
    if show == "S":
        show = True
        break
    if show == "N":
        show = False
        break
print(factorial(num,show))
