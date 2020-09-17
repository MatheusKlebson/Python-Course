#Exercício Python 72: Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20)
# mostrá-lo por extenso.
extenso = ("Zero","Um","Dois","Tres","Quatro",
          "Cinco","Seis","Sete","Oito",
          "Nove","Dez","Onze","Doze","Treze",
          "Quatorze","Quinze","Dezesseis","Dezssete",
          "Dezoito","Deznove","Vinte")
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 and num <= 20:
        print(f"O número {num} por extenso é {extenso[num]}")
    else:
        num = int(input("Digite corretamente senão não sairá o seu resultado por extenso\nNumero entre 0 e 20: "))
        if 0 <= num <= 20:
            print(f"O número {num} por extenso é {extenso[num]}")

    opção = " "
    while not opção in "SN":
        opção = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if opção == "N":
        break
print("Volte sempre!!")