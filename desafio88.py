from random import randint
from time import sleep
jogos = []
numeros = []
print('-' * 60)
print(f'{"GERADOR DE JOGOS DA MEGA SENA":^60}')
print('-' * 60)
j = int(input('Quantos jogos serão sorteados? '))
print(f'{"=" * 10} SORTEANDO {j} JOGOS {"=" * 10}')
for i in range(0, j):
    while True:
        num = randint(1, 60)
        if num not in numeros and len(numeros) <= 6:
            numeros.append(num)
        if len(numeros) == 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
for n in range(0, j):
    print(f'Jogo {n+1}: {jogos[n]}')
    sleep(1)
print(f'{"=" * 10} < BOA SORTE! > {"=" * 10}')