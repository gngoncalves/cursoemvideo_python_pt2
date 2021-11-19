v1 = int(input('Favor inserir um número inteiro: '))
cont = 'S'
soma = v1
vn = 0
c = 0
maior = menor = v1
while cont == 'S':
    c += 1
    soma += vn
    media = soma / c
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'S':
        vn = int(input('Favor inserir um número inteiro: '))
    if vn > maior:
        maior = vn
    elif vn == 0:
        menor = v1
    elif vn < menor:
        menor = vn
print('A média dos números inseridos é {:.2f}.'.format(media))
print('O maior número inserido foi o {} e o menor número inserido foi o {}.'.format(maior,menor))