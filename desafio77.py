palavras = ('Abobora', 'Abacate', 'Mamao', 'Paralelepipedo', 'Piao', 'Calendula')

for i in range(0, len(palavras)):
    print(f'A paravra {palavras[i].upper()} possui as seguintes vogais: ', end='')
    for p in palavras[i].lower():
        if p in 'aeiou':
            print(p, end=' ')
    print('')