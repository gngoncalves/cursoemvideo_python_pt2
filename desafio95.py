jogador = {}
qtdgols = []
jogadores = []
tgols = 0
while True:
    print('-' * 30)
    jogador['Nome'] = str(input('Nome do Jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for i in range(0, partidas):
        gol = int(input(f'Quantos gols foram feitos na partida {i+1}? '))
        tgols += gol
        qtdgols.append(gol)
    jogador['Gols'] = qtdgols[:]
    jogador['Total'] = tgols
    jogadores.append(jogador.copy())
    qtdgols.clear()
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).strip()[0]
        if cont in 'SsNn':
            break
        else:
            print('Opção Inválida. Tente novamente.')
    if cont in 'Nn':
        break
print('=' * 30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 30)
for k,v in enumerate(jogadores):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('=' * 30)
    cod = int(input(f'Mostrar dados de qual jogador? '))
    if cod == 999:
        break
    while True:
        if 0 <= cod <= len(jogadores)-1:
            print(f'Levantamento do Jogador {jogadores[cod]["Nome"]}:')
            for pos,i in enumerate(jogadores[cod]["Gols"]):
                print(f'No jogo {pos} fez {i} gols.')
            break
        else:
            print('Opção Inválida. Tente novamente.')
            break
print('Obrigado.')