#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapares = soma3coluna = maior2linha = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite o valor [{linha},{coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            somapares += matriz[linha][coluna]
print("="*30)
print("{:^30}".format("MATRIZ FORMADA"))
print("="*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end=" ")
    print()
print("="*30)
print("{:^30}".format("RESULTADOS"))
print("="*30)
print(f"Soma dos pares: {somapares}")   