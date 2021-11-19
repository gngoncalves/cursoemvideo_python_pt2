from random import randint
from time import sleep
from operator import itemgetter
game = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = {}
print(f'{"Valores sorteados":=^30}')
for k, v in game.items():
    print(f'O {k} tirou {v}.')
    sleep(1)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print(f'{"Ranking final":=^30}')
for i, v in enumerate(ranking):
    print(f'{i}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)
