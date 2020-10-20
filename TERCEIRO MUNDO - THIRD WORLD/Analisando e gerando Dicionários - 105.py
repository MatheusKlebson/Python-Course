# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
'''– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)'''
def notes(*n):
    notebook = dict()
    notebook["NotesTotal"] = len(n)
    notebook["FisrtNote"] = max(n)
    notebook["LastNote"] = min(n)
    return notebook


response = notes(10,5,3,4)
print(response)