#  Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#  o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#  indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(calcular,show):
    print("="*50)
    if show == True:
        f = 1
        for c in range(calcular,0,-1):
            f *= c
            print(f"{c}", end="")
            if c > 1:
                print(" X ", end="")
            else:
                print(" = ", end="")
        return f
    else:
        f = 1
        for c in range(calcular,0,-1):
            f *= c
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

print(fatorial(num,show))
