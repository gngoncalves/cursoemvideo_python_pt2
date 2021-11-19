from time import sleep
from random import randint


def Sorteio(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        sort = randint(0, 10)
        sleep(0.5)
        print(sort, end=' ')
        lst.append(sort)
    print('FINALIZADO.')

def SomaPar(lst):
    soma = 0
    for l in lst:
        if l % 2 == 0:
            soma += l
    print(f'Somando os valores pares de {lst}, temos {soma}.')


lista = []
Sorteio(lista)
SomaPar(lista)