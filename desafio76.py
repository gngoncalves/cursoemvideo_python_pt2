itens = ('Arroz', 6.99, 'Peito de Frango', 15.00, 'Carne', 19.99, 'Veja X-14', 12.99)
print('=' *60)
print('{:^50}'.format('TABELA DE PREÇOS'))
print('=' * 60)
for i in range(0, len(itens),2):
    print(f'{itens[i]:.<20}{"."*32:<32}R$ {itens[i+1]:>5.2f}')