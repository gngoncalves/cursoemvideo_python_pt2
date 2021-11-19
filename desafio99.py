from time import sleep
def decorator():
    print('=' * 90)


def maiorvalor(*num):
    maior = 0
    decorator()
    print('Analisando os Valores Inseridos...')
    print('Os valores inseridos foram: ', end='')
    for i in num:
        print(i, end=' ')
        if i >= maior:
            maior = i
        sleep(0.5)
    print(f'Foram informados {len(num)} números ao todo.')
    print(f'O maior valor informado foi {maior}.')


maiorvalor(1, 3, 12, 26, 0)
maiorvalor(90, 2, 78)
maiorvalor()
