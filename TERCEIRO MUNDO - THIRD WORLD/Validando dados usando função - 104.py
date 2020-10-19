# Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = num 
            ok = True
        else:
            print("ERRO!! Não é um número...")
        if ok == True:
            break
    return valor


#Programa principal
num = leiaInt("Digite um número: ")
print(f"O número digitado foi {num}")
