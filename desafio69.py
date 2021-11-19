maior = homem = mulher = 0
while True:
    idade = int(input('Insira a idade: '))
    while True:
        sexo = str(input('Insira o sexo [M/F]: ')).strip()[0]
        if sexo in 'Mm' or sexo in 'Ff':
            break
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Mm' and idade < 20:
        mulher += 1
    while True:
        cont = str(input('Deseja continuar [S/N]? ')).strip()[0]
        print('=' * 40)
        if cont in 'Ss' or cont in 'Nn':
            break
    if cont in 'Nn':
        break
print(f'{maior} pessoas possuem mais de 18 anos.')
print(f'Exitem {homem} homens cadastrados nesta relação.')
print(f'Existem {mulher} mulheres com menos de 20 anos.')