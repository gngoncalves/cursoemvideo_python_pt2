lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    while True:
        cont = str(input('Deseja Continuar[S/N]? ')).strip()[0]
        if cont in 'SsNn':
            break
        else:
            print('Opção Inválida. Digite novamente.')
    if cont in 'Nn':
        break
print('=-=' * 20)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'O números inseridos em formato decrescente foram: {lista}.')
if 5 in lista:
    print('O valor 5 encontra-se na lista!')
else:
    print('O valor 5 não se encontra na lista!')