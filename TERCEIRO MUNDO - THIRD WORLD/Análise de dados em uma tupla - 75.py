#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
# guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
valores = (int(input("Primeiro valor: ")),
           int(input("Segundo valor: ")),
           int(input("Terceiro valor: ")),
           int(input("Quarto valor: ")))
print("Valores digitados: {}".format(valores))
print("="*50)
print(f"O número 9 apareceu {valores.count(9)} vezes")
print("="*50)
totpar = 0
if 3 in valores:
    print(f"o número 3 foi encontrado na {valores.index(3) + 1}º posição")
else:
    print("O número 3 não foi digitado NENHUMA VEZ")
print("="*50)
print("O números pares digitados: ",end="")
for cont in range(0,len(valores)):
    if valores[cont] % 2 == 0:
        print(valores[cont],end=" ")
        totpar +=1
print(f"\nTotal de pares foram: {totpar}")