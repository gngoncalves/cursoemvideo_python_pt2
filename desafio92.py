from datetime import date
cadastro = {'Nome' : str(input('Nome: ')).strip(),
            'Idade' : date.today().year - int(input('Ano de Nascimento: ')),
            'CTPS' : int(input('Número da CTPS (0, caso não tenha): '))}
if cadastro['CTPS'] != 0:
    cadastro['Contratação'] = int(input('Qual o ano de contratação: '))
    cadastro['Salário'] = float(input('Qual o salário de contratação: R$'))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] + 35) - (date.today().year - cadastro['Idade'])
print('=' * 30)
for k, v in cadastro.items():
    print(f'O {k} tem valor {v}.')