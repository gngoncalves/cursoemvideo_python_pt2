from time import sleep
alunos = []
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    alunos.append([nome,n1,n2,media])
    while True:
        cont = str(input('Deseja continuar? [S/N] ')).strip()[0]
        if cont in 'NnSs':
            break
        else:
            print('Opção inválida. Tente novamente.')
    if cont in 'Nn':
        break
print('=' * 40)
print(F'Nº {"NOME":<10} {"MÉDIA":>10}')
print('-' * 40)
for i in range(0, len(alunos)):
        print(f'{i:<2} {alunos[i][0]:<10} {alunos[i][3]:>10.1f}')
print('-' * 40)
while True:
    notas = int(input('Mostrar notas de qual aluno? (Pressione 999 para interromper): '))
    if notas <= len(alunos) - 1:
        print(f'As notas de {alunos[notas][0]} são {alunos[notas][1:3]}')
    elif notas == 999:
        print('FINALIZANDO...')
        break
    else:
        print('Opção Inválida. Selecione a opção que corresponda ao aluno desejado.')
    print('-' * 60)
sleep(1)
print('Programa Finalizado com Sucesso.')