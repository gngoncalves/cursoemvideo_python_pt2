tupla = (int(input('Digite um número [1/4]: ')), int(input('Digite um número [2/4]: ')),
         int(input('Digite um número [3/4]: ')), int(input('Digite um número [4/4]: ')))
print(f'Você digitou os seguintes valores: {tupla}.')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 not in tupla:
    print('O número 3 não foi digitado em nenhuma posição.')
else:
    print(f'O número 3 foi digitado na {tupla.index(3)+1}ª posição.')
print('Os valores pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
