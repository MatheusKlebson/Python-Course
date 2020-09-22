#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 
#preencha com valores lidos pelo teclado. No final, 
#mostre a matriz na tela, com a formatação correta.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite o valor [{linha},{coluna}]: "))
print("="*30)
print("{:^30}".format("MATRIZ FORMADA"))
print("="*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
    print()