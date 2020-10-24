# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
'''– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)'''
def notes(*num):
     '''
    FUNCTION FOR CALCULATING MANY NUMBERS:
    def(*num,situation=False) 
    RECEIVES PARAMETERS
    (ACCEPT MANY NUMBERS) *n = numbers 
    (OPTIONAL PARAMETER) situation = medium situation
    RETURN DICTIONARY
    '''
    dictionary = dict()
    dictionary["NOTES_TOTAL"] = len(num)
    dictionary["MAXIMUM_NOTE"] = max(num)
    dictionary["MINIMUM_NOTE"] = min(num)
    dictionary["CLASS_AVERAGE"] = sum(num)/len(num)
    if dictionary["CLASS_AVERAGE"] >= 7 and dictionary["CLASS_AVERAGE"] <= 10:
        dictionary["SITUATION"] = "Very Good"
    elif dictionary["CLASS_AVERAGE"] >= 5 and dictionary["CLASS_AVERAGE"] < 7:
        dictionary["SITUATIOM"] = "Reasonable"
    elif dictionary["CLASS_AVERAGE"] >= 0 and dictionary["CLASS_AVERAGE"] < 5:
        dictionary["SITUATIOM"] = "Very Bad"
    else:
        dictionary["SITUATIOM"] = "Medium Invalid"
    return dictionary




