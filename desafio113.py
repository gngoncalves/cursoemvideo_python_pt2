def leiaInt(num):
    while True:
        try:
            n1 = int(input(num))
        except KeyboardInterrupt:
            n1 = 0
            print('O usuário preferiu não digitar esse número.')
            break
        except:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n1


def leiaFloat(num):
    while True:
        try:
            n2 = float(input(num))
        except KeyboardInterrupt:
            n2 = 0
            print('O usuário preferiu não digitar esse número.')
            break
        except:
            print('\033[31mErro! Digite um número real válido.\033[m')
            continue
        else:
            return n2


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}.')