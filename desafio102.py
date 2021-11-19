def fatorial(n, show=False):
    """
    Cálculo de fatorial.
    :param n: Valor do fatorial a ser calculado.
    :param show: Indicação se deseja mostrar o processo de cálculo do fatorial.
    :return: valor do Fatorial calculado.
    """
    f = 1
    for i in range(n, 0, -1):
        if show == True:
            if i > 1:
                print(i, end=' x ')
            else:
                print(i, end=' = ')
        f *= i
    return f

num = int(input('Deseja calcular o fatorial de qual número? '))
while True:
    op = str(input('Deseja ver o processo de cálculo do Fatorial? [S/N] ')).strip()[0]
    if op in 'NnSs':
        if op in 'Nn':
            show = False
            break
        else:
            show = True
            break
    else:
        print('Opção Inválida. Tente Novamente.')
print(fatorial(num, show))