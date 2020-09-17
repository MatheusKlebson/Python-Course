#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário
# mostre seu novo salário, com 15% de aumento.
salario = float(input("Salário do funcionario:R$"))
aumento = salario + (salario*15/100)
print("Com aumento de 15% o seu salário passará a ser",aumento,"R$")