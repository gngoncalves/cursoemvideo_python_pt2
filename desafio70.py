p = total = 0
barato = ''
menorpreco = 0
while True:
    nome = str(input('Insira o nome do produto: '))
    preco = float(input('Insira o preço do produto: R$'))
    total += preco
    if preco >= 1000:
        p += 1
    if menorpreco == 0 or menorpreco > preco:
        menorpreco = preco
        barato = nome
    while True:
        cont = str(input('Deseja continuar [S/N]? ')).strip()[0]
        print('=' * 40)
        if cont in 'Ss' or cont in 'Nn':
            break
    if cont in 'Nn':
        break
print(f'O total gasto nesta compra foi de R${total:.2f}.')
print(f'{p} produtos custaram acima de R$1000.00.')
print(f'O produto mais barato é o {barato}, com o valor de R${menorpreco:.2f}.')