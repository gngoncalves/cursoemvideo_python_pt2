def mensagem(msg):
    t = len(msg)
    print(t * '~')
    print(msg)
    print(t * '~')


mensagem(f'{"Olá":^5}')
mensagem(f'{"Testando o código":^30}')