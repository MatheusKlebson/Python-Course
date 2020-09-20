#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista = []
for cont in range(0,5):#For que contará os valores até 5
  num = int(input(f"Digite {cont}º valor: ")) #Variavel que guardará os valores digitados
  if cont == 0 or num > lista[-1]: #Condição que colocará esse valor sempre na ultima posição por ser sempre o maior
    lista.append(num) 
    print("Adicionado ao fim")
  else:
    pos = 0
    while pos < len(lista):
      if num <= lista[pos]:
        lista.insert(pos,num)
        print(f"Adicionado na posição {pos}...")
        break
      pos = pos + 1
print("="*30)
print(f"Lista criada: {lista}")