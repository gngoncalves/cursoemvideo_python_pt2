lista = []
lpar = []
limpar = []
while True:
    num = int(input('Insira um número: '))
    lista.append(num)
    while True:
        cont = str(input('Deseja Continuar[S/N]? ')).strip()[0]
        if cont in 'SsNn':
            break
        else:
            print('Opção Inválida. Tente Novamente.')
    if cont in 'Nn':
        break
for i in lista:
    if i % 2 == 0:
        lpar.append(i)
    else:
        limpar.append(i)
print(f'''
A lista original é: {lista}.
A lista de números pares é: {lpar}.
A lista de números ímpares é: {limpar}.
''')