from time import sleep
c = 1
while True:
    num = int(input('Insira um número, para calcular a sua tabuada: '))
    print('-' * 50)
    if num < 0:
        break
    print(f'Tabuada de {num}:')
    while c <= 10:
        p = num * c
        print(f'{num} x {c:2} = {p:2}')
        c += 1
    print('-' * 50)
    c = 1
print('Finalizando...')
sleep(1)
print('Programa Finalizado.')