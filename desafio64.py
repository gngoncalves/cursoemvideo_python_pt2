num = int(input('Digite um número inteiro [Digite 999 para parar]: '))
soma = 0
count = 0
while num != 999:
    soma += num
    num = int(input('Digite um número inteiro [Digite 999 para parar]: '))
    count += 1
print('A quantidade de números inseridos foi de {} e a soma dos números inseridos foi de {}.'.format(count,soma))
