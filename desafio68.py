from random import randint
print('Vamos jogar PAR ou ÍMPAR!')
c = 0
while True:
    npc = randint(0, 10)
    player = int(input('Insira um número para jogarmos: '))
    soma = player + npc
    while True:
        opcao = str(input('Qual a sua opção? PAR ou Ímpar [P/I] ')).strip().upper()[0]
        if opcao == 'P' or opcao == 'I':
            break
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {player} e o computador jogou {npc}. Total de {soma}. É {resultado}.')
    print('-' * 30)
    if opcao == 'P' and resultado == 'PAR':
        print('Parabéns! Você ganhou!')
        c += 1
        print('Vamos jogar novamente!')
        print('=' * 30)
    elif opcao == 'I' and resultado == 'ÍMPAR':
        print('Parabéns! Você ganhou!')
        c += 1
        print('Vamos jogar novamente!')
        print('=' * 30)
    else:
        break
print('You Lose.')
print(f'Você venceu {c} vez(es) a máquina antes de perder.')