extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Insira um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você selecionou o número {extenso[num]}.')
        cont = str(input('Deseja continuar [S/N]?')).strip()[0]
        if cont in 'Nn':
            break
    else:
        print('Número inválido. Tente novamente.')