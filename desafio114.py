import urllib.request
try:
    urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está disponível.')
else:
    print('Tudo certo, site em funcionamento.')