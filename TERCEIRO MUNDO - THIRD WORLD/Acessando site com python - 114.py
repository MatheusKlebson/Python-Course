'''Exercício Python 114: Crie um código em Python que teste se 
o site pudim está acessível pelo computador usado.'''
import urllib
import urllib.request
try:
    acesso = urllib.request.urlopen("http://www.google.com.br")
except urllib.error.URLError:
    print("The web is not available")
else:
    