#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#Abaixo de 5.0 = Reprovado
#Entre 5.0 e 6.9 = Recuperação
#7.0 acima = Aprovado
n1 = float(input("Primeira nota: ")) #Ler primeira nota
n2 = float(input("Segunda nota: ")) #Ler segunda nota
media = (n1+n2)/2 #Variavel que calcula qual é a media
print(f"A media do aluno: {media}") #mostrar media na tela
 #Primeira condição (Aprovado)
if media >= 7 and media <= 10:
    print("Aluno: Aprovado") #Mostrar caso o aluno seja aprovado
 #Segunda condição (Recupeção)
elif media >= 5 and media < 7:
    print("Aluno: Recuperação") #Mostrar caso o aluno fique na recuperação
 #terceira condição (Reprovado)
elif media >= 0 and media < 5:
    print("Aluno: Reprovado") #Mostrar caso o aluno seja reprovado
else:  #Condição caso as outras não sejam atendidas
    print("Nota inexistente")