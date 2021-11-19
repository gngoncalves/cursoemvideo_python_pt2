brasileirao = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'RB Bragantino', 'Fortaleza',
               'Corinthians', 'Internacional', 'Fluminense', 'Cuiabá', 'América-MG',
               'Atlético-GO', 'São Paulo', 'Ceará', 'Athletico-PR', 'Santos',
               'Bahia', 'Sport', 'Juventude', 'Grêmio', 'Chapecoense')
print('='*100)
print(f'O G5 do Brasileirão 2020 é: {brasileirao[:5]}')
print('='*100)
print(f'O Z4 do Brasileirão 2020 é: {brasileirao[-4:]}')
print('='*100)
print('Ordenação por ordem alfabética: ',sorted(brasileirao))
print('='*100)
print(f'A Chapecoense está no {brasileirao.index("Chapecoense")+1}º lugar.')