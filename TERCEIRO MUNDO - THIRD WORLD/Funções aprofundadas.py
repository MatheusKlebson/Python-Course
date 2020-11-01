'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
def leiaInt(mensagem):
    while True:
        try:
            num = int(input(mensagem))
        except (ValueError,TypeError):
            print("ERRO!! Por favor digite um valor inteiro...")
        except (KeyboardInterrupt):
            print("O usuário interropeu o programa, o valor será nulo.")
            return 0
            break
        else:
            return num
            break

num_int = leiaInt("Digite um número inteiro: ")
print(f"O número inteiro: {num_int}")