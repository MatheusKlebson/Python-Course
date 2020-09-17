#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input("Informe o sexo[M/F]: ")).strip().upper()[0] #Variavel que guardará o valor do sexo
#Condição caso o usuario digite errado
while not sexo in "MF":
    sexo = str(input("Informe corretamente o sexo[M/F]: ")).strip().upper()[0] #Variavel que aparecerá para que o usuario digite corretamente
print(f"Sexo [{sexo}] informado com sucesso!!") #Mostre na tela o sexo informado