print('=' * 40)
print('{:^40}'.format('Banco Fictício'))
print('=' * 40)
quant = int(input('Informe a quantia necessária para saque: R$'))
c50 = quant // 50
r50 = quant % 50
c20 = r50 // 20
r20 = r50 % 20
c10 = r20 // 10
r10 = r20 % 10
c01 = r10 // 1
print('Serão fornecidos: ')
if c50 > 0:
    print(f'Total de {c50} notas de R$50.00.')
if c20 > 0:
    print(f'Total de {c20} notas de R$20.00.')
if c10 > 0:
    print(f'Total de {c10} notas de R$10.00.')
if c01 > 0:
    print(f'Total de {c01} notas de R$1.00.')
print('=' * 40)

print('Muito obrigado por ser um cliente nosso. Volte sempre!')