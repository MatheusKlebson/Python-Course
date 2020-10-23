# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
# Ex:                                                      
# escreva(‘Olá, Mundo!’) Saída:                                                                                                                          
# ~~~~~~~~~                                                                                                                                                            
# Olá, Mundo!                                                                                                                                                          
# ~~~~~~~~~  
def write(text):
    size = len(text) + 4
    print("="*size)
    print(f"  {text}")
    print("="*size)

write("HELLO WORLD")
write("I AM PROGRAMMER")