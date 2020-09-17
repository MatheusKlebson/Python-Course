#Exercício Python 026: Faça um programa que leia uma frase pelo teclado
#mostre quantas vezes aparece a letra "A"
#em que posição ela aparece a primeira vez
#em que posição ela aparece a última vez.
from time import sleep
frase = str(input("Frase: ")).strip().upper()
print("Analisando...")
sleep(2)
print("A frase possui {} letras [A]".format(frase.count("A")))
print("A primeira letra [A] se encontra na posição {}".format(frase.find("A")+1))
print("A última letra [A] se encontra na posição {}".format(frase.rfind("A")+1))

