dados = {}
dados['Nome'] = str(input('Nome do Jogador: ')).strip()
partidas = int(input(f'Quantas partidas o {dados["Nome"]} jogou?'))
gols = []
print('=' * 50)
for p in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {p}? '))
    gols.append(gol)
dados['Gols'] = gols
dados['Total'] = sum(gols)
print('=' * 50)
print(dados)
print('=' * 50)
for k, v in dados.items():
    print(f'O campo {k}, tem o valor {v}.')
print('=' * 50)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for g in range(0, len(dados['Gols'])):
    print(f'    -> Na partida {g}, fez {dados["Gols"][g]} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
