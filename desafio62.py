a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
n = 1
total = 0
add = 10
while add != 0:
    total = add + total
    while n <= total:
        an = a1 + (n - 1) * r
        print(an, end= ' >> ')
        n += 1
    print('Pausa')
    add = int(input('Gostaria de ver mais termos? '))
print('Finalizado com {} termos.'.format(total))