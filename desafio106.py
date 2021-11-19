def ajuda():
    while True:
        msg = 'SISTEMA DE AJUDA PYHELP'
        t = len(msg) + 4
        print('\033[46m', end='')
        print(t * '~')
        print(f'  {msg}')
        print(t * '~')
        opt = str(input('\033[mFunção ou Biblioteca > ')).lower()
        if opt == 'fim':
            bye = 'ATÉ LOGO!'
            t2 = len(bye) + 4
            print('\033[41m', end='')
            print(t2 * '~')
            print(f'  {bye}')
            print(t2 * '~')
            break
        tit = f"Acessando o manual do comando '{opt}'"
        t1 = len(tit) + 4
        print('\033[41m', end='')
        print(t1 * '~')
        print(f'  {tit}')
        print(t1 * '~')
        print("\033[m\033[7m", end='')
        help(opt)
        print('\033[m', end='')


ajuda()