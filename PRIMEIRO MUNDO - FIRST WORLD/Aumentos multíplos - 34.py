#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Salário do funcionario:R$"))
if salario > 1250:
    aumento = salario + (salario*10/100)
    print("Aumento de 10%: {:.2f}R$".format(aumento))
else:
    aumento = salario + (salario*15/100)
    print("Aumento de 15%: {:.2f}R$".format(aumento))
