matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = ml2 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna]=(int(input(f'Insira um valor para a posição [{linha}, {coluna}]: ')))
print('=' * 60)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^4}]', end= ' ')
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
        if coluna == 2:
            scol += matriz[linha][coluna]
        if linha == 1 and ml2 == 0:
            ml2 = matriz[linha][coluna]
        elif linha == 1 and matriz[linha][coluna] >= ml2:
            ml2 = matriz[linha][coluna]
    print()
print('=' * 60)
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira coluna é {scol}.')
print(f'O maior valor da segunda linha é {ml2}.')