numeros = []
for i in range(1,6):
    num = int(input(f'Insira um número [{i}/5]: '))
    numeros.append(num)
print(f'Os números inseridos foram: {numeros}.')
print(f'O menor valor inserido foi o {min(numeros)}, na posição ', end='')
for n in range(0, len(numeros)):
    if numeros[n] == min(numeros):
        print(f'{n}...', end=' ')
print(f'\nO maior valor inserido foi o {max(numeros)}, na posição ', end='')
for p in range(0, len(numeros)):
    if numeros[p] == max(numeros):
        print(f'{p}...', end= ' ')
print('\nFinalizado.')