# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
'''– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)'''
def notes(*n,situation=False):
    '''
    FUNCTION FOR CALCULATING MANY NUMBERS:
    def(*n,situation=False) 
    RECEIVES PARAMETERS
    (ACCEPT MANY NUMBERS) *n = numbers 
    (OPTIONAL PARAMETER) situation = medium situation
    RETURN DICTIONARY
    '''
    notebook = dict()
    notebook["NotesTotal"] = len(n)
    notebook["FisrtNote"] = max(n)
    notebook["LastNote"] = min(n)
    notebook["Medium"] = sum(n)/len(n)
    if situation == True:
        if notebook["Medium"] >= 7 and notebook["Medium"] <= 10:
            notebook["Situation"] = "Very Good"
        elif notebook["Medium"] >= 5 and notebook["Medium"] < 7:
            notebook["Situation"] = "Reasonable"
        elif notebook["Medium"] >= 0 and notebook["Medium"] < 5:
            notebook["Situation"] = "Very bad"
        else:
             notebook["Situation"] = "Medium invalid"
    return notebook


response = notes(10,8,7,situation=True)
print(response)