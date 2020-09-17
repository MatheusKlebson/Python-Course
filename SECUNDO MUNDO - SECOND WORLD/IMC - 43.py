#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#MENOR QUE 18,5	MAGREZA
#ENTRE 18,5 E 24,9	NORMAL
#ENTRE 25,0 E 29,9	SOBREPESO
#ENTRE 30,0 E 39,9	OBESIDADE
#MAIOR QUE 40,0	OBESIDADE GRAVE
from time import sleep
print("="*15)
print("CALCULANDO IMC")
print("="*15)
peso = float(input("PESO DA PESSOA:"))
altura = float(input("ALTURA DA PESSOA:"))
imc = peso/(altura**2)
print("Analisando...")
print(f"IMC: {imc}")
sleep(2)
if imc < 18.5:
    print("IMC: MAGREZA")
elif imc >= 18.5 and imc <= 24.9:
    print("IMC: NORMAL")
elif imc >= 25 and imc < 30:
    print("IMC: SOBREPESO")
elif imc >= 30 and imc < 40:
    print("IMC: OBESIDADE")
elif imc >= 40:
    print("IMC: OBESIDADE GRAVE")
else:
    print("IMC INVÁLIDO")