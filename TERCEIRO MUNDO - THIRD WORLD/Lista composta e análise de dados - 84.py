#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.                                                                                                    
# C) Uma listagem com as pessoas mais leves.
dados = []
pessoas = list()
'''Lista dados para guardar informações e a lista pessoas para copiar'''
pesado = leve = 0
totpesado = totleve = 0
'''Variaveis para os mais leves e pesados'''
print("="*50)
print("{:^50}".format("Cadastrando pessoas"))
print("="*50)
while True:
  dados.append(str(input("Nome: ")))
  dados.append(float(input("Peso: ")))
  '''Guardando nos dados'''
  if len(pessoas) == 0:
    pesado = dados[1]
    leve = dados[1]
  else:
    if dados[1] > pesado:
      pesado = dados[1]
    if dados[1] < leve:
      leve = dados[1]
  '''Analisa o comprimento da lista pessoas para tirar o mais pesado e o mais leve'''
  pessoas.append(dados[:])
  dados.clear()
  '''Copia e limpa dados'''
  opção = " "
  while not opção in "SN":
      opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
  if opção == "N":
      break
print("="*50)
print("{:^50}".format(f"Total cadastrados = {len(pessoas)}"))
print("="*50)
print("="*50)
print("{:^50}".format("Fim do cadastro"))
print("="*50)
print(f"Mais pesado: {pesado: <8}",end=" ")
for p in pessoas:
  if p[1] == pesado:
    totpesado += 1
if totpesado > 1:
  print("Nome das pessoas: ",end=" ")
else:
  print("Nome da pessoa: ",end=" ")

for p in pessoas:
  if p[1] == pesado:
    print(f"[{p[0]}]",end="")    

print(f"\nMais leve: {leve: <10}",end=" ")
for p in pessoas:
  if p[1] == leve:
    totleve += 1
if totleve > 1:
  print("Nome das pessoas: ",end=" ")
else:
  print("Nome da pessoa: ",end=" ")

for p in pessoas:
  if p[1] == leve:
    print(f"[{p[0]}]",end="")