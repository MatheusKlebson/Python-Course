#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.
palavras = ("MATHEUS","ISIS","AMOR","MOZAO",
            "AMORZINHO","AMORE","MOH")
for p in palavras:
    print(f"\nPara a palavra {p} temos as vogais: ",end="")
    for vogal in p:
        if vogal in "AEIOU":
            print(f"{vogal}",end=" ")