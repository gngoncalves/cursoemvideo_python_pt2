def cab(msg):
    print(msg)
    print(len(msg) * '-')


def area(l1, l2):
    s = l1 * l2
    print(f'A área de um terreno de {l1} x {l2} é de {s} m2.')


cab('Controle de Terrenos')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))