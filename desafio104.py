def leiaInt(num):
    while True:
        n1 = str(input(num))
        if n1.isnumeric():
            n1 = int(n1)
            return n1
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}.')