lista = []
while True:
    num = int(input('Insira um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Número já cadastrado. O mesmo não será inserido.')
    while True:
        cont = str(input('Deseja continuar [S/N]? ')).strip()[0]
        if cont in 'SsNn':
            break
        else:
            print('Opção Inválida.')
    if cont in 'Nn':
        break
print('=-=' * 20)
lista.sort()
print(f'Os valores digitados foram: {lista}.')
