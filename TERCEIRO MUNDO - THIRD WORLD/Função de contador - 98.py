''' Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
 que receba três parâmetros: início, fim e passo. 
 Seu programa tem que realizar três contagens através da função criada:                
 a) de 1 até 10, de 1 em 1                                                                                                                                              
 b) de 10 até 0, de 2 em 2                                                                                                                                            
 c) uma contagem personalizada'''
from time import sleep
def mostraLinha(txt):
    print("="*30)
    print(txt)
def contador(inicio,fim,passo):
    if fim > 0:
        for c in range(inicio,fim + 1,passo):
            print(c,end=" ")
            sleep(1)
        print("FIM")
    else:
        for c in range(inicio,fim - 1,passo):
            print(c,end=" ")
            sleep(1)
        print("FIM")
mostraLinha("CONTAGEM DE 1 A 10 DE 1 EM 1")
contador(1,10,1)
mostraLinha("CONTAGEM DE 10 A 0 DE 2 EM 2")
contador(10,0,-2)
print("="*30)
print("Agora é sua vez de personalizar...")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
if i > f and p > 0:
    dobro = p
    dobro *= 2
    p = p - dobro 
    mostraLinha(f"CONTAGEM DE {i} A {f} DE {p + dobro} EM {p + dobro}")
else:
    mostraLinha(f"CONTAGEM DE {i} A {f} DE {p} EM {p}")
contador(i,f,p)