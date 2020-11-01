'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(mensagem):
    ok = False
    while ok == False:
        try:
            num = int(input(mensagem))
        except (ValueError,TypeError):
            print(f"ERRO!!! escreva um número inteiro...")
        else:
            ok = True
            return num
            if ok == True:
                break

n1 = leiaInt("Digite um número inteiro: ")
#n2 = leiaFloat("Digite um número real:")