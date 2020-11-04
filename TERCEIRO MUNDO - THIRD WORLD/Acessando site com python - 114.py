import urllib
import urllib.request
try:
    acesso = urllib.request.urlopen("http://www.google.com.br")
except urllib.error.URLError:
    print("The web is not available")
else:
    print("The web is available")
    