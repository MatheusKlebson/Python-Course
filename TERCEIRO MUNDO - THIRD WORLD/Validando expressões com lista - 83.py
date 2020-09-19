#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
# abertos e fechados na ordem correta.
lista = []
print("Exemplo de expressão: (a + b) - 5 = (c * 2)")
expressao = str(input("Crie uma expressão: "))
for simbolos in expressao:
    if simbolos == "(":
        lista.append("(")
    elif simbolos == ")":
        lista.append(")")
if lista.count("(") == lista.count(")"):
    print("EXPRESSÃO VÁLIDA")
else:
    print("EXPRESSÃO INVÁLIDA")
    print(f"Total de parênteses aberto: {lista.count('(')}")
    print(f"Total de parênteses fechado: {lista.count(')')}")
