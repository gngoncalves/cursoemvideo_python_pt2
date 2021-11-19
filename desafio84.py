lista1 = []
cadastro = []
maior = menor = 0
while True:
    lista1.append(str(input('Nome: ')).strip())
    lista1.append(float(input('Peso: ')))
    cadastro.append(lista1[:])
    lista1.clear()
    while True:
        cont = str(input('Deseja Continuar? [S/N] '))[0]
        if cont in 'SsNn':
            break
    if cont in 'Nn':
        break
for p in cadastro:
    if maior == 0 and menor == 0:
        maior = menor = p[1]
    elif p[1] >= maior:
        maior = p[1]
    elif p[1] <= menor:
        menor = p[1]
print(f'Foram cadastradas {len(cadastro)} pessoas no total.')
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for men in cadastro:
    if men[1] == menor:
        print(f'{men[0]}', end=' ')
print()
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for mai in cadastro:
    if mai[1] == maior:
        print(f'{mai[0]}', end=' ')