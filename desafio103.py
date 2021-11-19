def ficha(nome='<desconhecido>', g=0):
    print(f'O jogador {nome} fez {g} gol(s) no campeonato.')


print('-' * 40)
jogador = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == "":
    ficha(g=gols)
else:
    ficha(jogador,gols)