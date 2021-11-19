from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
menor = maior = tupla[0]
print('A tupla gerada automaticamente foi: ', end='')
for i in tupla:
    print(i, end=' ')
print('')
for c in tupla: #Também podemos usar as funções max() e min(), mas fiz com estrutura de repetição para fixar.
    if c < menor:
        menor = c
    elif c > maior:
        maior = c
print(f'O menor número gerado foi o número {menor}.')
print(f'O maior número gerado foi o número {maior}.')
