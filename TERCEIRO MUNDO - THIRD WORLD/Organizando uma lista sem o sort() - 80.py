#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
#cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
numbers = []
for accountant in range(0,5):
  num = int(input(f"Write a number: "))
  if accountant == 0 or num > numbers[-1]:
    numbers.append(num)
    print(f"The number placed in the last position in the list...")
  else:
    position = 0
    while position < len(numbers):
      if num <= numbers[position]:
        numbers.insert(position,num)
        print(f"The number placed in the {position} position in the list...")
        break
      position += 1
print(f"List create: {numbers}")
