matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um número para a posição [{linha}, {coluna}]: '))
        matriz[linha][coluna] = num
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^4}]', end='')
    print()