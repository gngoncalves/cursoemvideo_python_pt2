pessoas = {}
grupo = []
somaidade = 0
while True:
    pessoas['Nome'] = str(input('Nome: ')).strip()
    while True:
        sexo = str(input('Sexo: ')).strip().upper()[0]
        if sexo in 'MF':
            pessoas['Sexo'] = sexo
            break
        print('Opção Inválida. Tente Novamente.')
    pessoas['Idade'] = int(input('Idade: '))
    somaidade += pessoas['Idade']
    grupo.append(pessoas.copy())
    while True:
        cont = str(input('Deseja Continuar? [S/N] ')).strip()[0]
        if cont in 'NnSs':
            break
        print('Opção inválida. Tente novamente.')
    if cont in 'Nn':
        break
media = somaidade / len(grupo)
print('=' * 40)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for pos,i in enumerate(grupo):
    for k,v in i.items():
        if v == 'F':
            print(f'{i["Nome"]}', end=' ')
print()
print('- Lista das pessoas que estão acima da média:')
for pos,i in enumerate(grupo):
    for k,v in i.items():
        if i['Idade'] >= media:
            print(f'{k} = {v}', end='; ')
    print()
