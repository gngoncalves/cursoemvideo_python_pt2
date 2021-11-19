aluno = {}
aluno['Nome'] = str(input('Nome: ')).strip()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = '\033[32mAprovado\033[m'
else:
    aluno['Situação'] = '\033[31mReprovado\033[m'
for k, v in aluno.items():
    print(f'{k} é igual a {v}.')
