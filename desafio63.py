n = int(input('Digite a quantidade de elementos da sequência de fibonacci: '))
cont = 3
f0 = 0
f1 = 1
fn = 0
while cont <= n:
    if cont == 3:
        fn = f0 + f1
        print('{} >> {} >> {}'.format(f0,f1,fn), end=' >> ')
        f0 = f1
        f1 = fn
        cont += 1
    else:
        fn = f0 + f1
        print('{}'.format(fn), end= ' >> ')
        f0 = f1
        f1 = fn
        cont += 1
print('FIM')