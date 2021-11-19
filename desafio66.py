c = 0
soma = 0
while True:
    num = int(input('Insira um número (Digite 999 para parar): '))
    if num == 999:
        break
    soma += num
    c += 1
print(f'Foram inseridos {c} número(s), totalizando uma soma de {soma}.')
