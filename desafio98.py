from time import sleep
def decorator():
    print('=-' * 20)


def contador(inicio, fim, passo):
    decorator()
    print(f'Contagem de {inicio} até {fim} de', end=' ')
    if passo < 0:
        print(f'{passo * -1} em {passo * -1}.')
        fim -= 1
    if fim > inicio and passo > 0:
        print(f'{passo} em {passo}.')
        fim += 1
    elif inicio > fim and passo > 0:
        print(f'{passo} em {passo}.')
        passo *= -1
        fim -= 1
    if passo == 0 and inicio > fim:
        print('de 1 em 1.')
        passo = -1
        fim -= 1
    elif passo == 0 and fim > inicio:
        print('de 1 em 1.')
        passo = 1
        fim += 1
    for i in range(inicio, fim, passo):
        print(i, end=' ')
        sleep(0.5)
    print('FIM.')


contador(0, 10, 1)
contador(10, 0, 2)
decorator()
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input(f'{"Início: ":<7}'))
fim = int(input(f'{"Fim: ":<7}'))
pas = int(input(f'{"Passo: ":<7}'))
contador(ini, fim, pas)