'''Exercício Python 114: Crie um código em Python que teste se 
o site pudim está acessível pelo computador usado.'''
import urllib
import urllib.request
try:
    site = urllib.request.urlopen("http://www.google.com.br")
except urllib.error.URLError:
    print("A internet não está disponível")
else:
    print("A internet tá funcionando tranquilamente")