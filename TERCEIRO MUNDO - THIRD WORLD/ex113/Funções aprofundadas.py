'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''
import validação

num_int = validação.leiaInt("Digite um número inteiro: ")
num_real = validação.leiaFloat("Digite um número real: ")
print(f"O número Inteiro: {num_int}")
print(f"O número real: {num_real}")