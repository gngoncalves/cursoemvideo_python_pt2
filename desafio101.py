def voto(ano):
    """
    :param i: representa o valor da idade a ser analisada na função.
    :return: retorna a resposta condicional em relação à idade inserida.
    """
    from datetime import date
    v = ''
    idade = date.today().year - ano
    if idade < 16:
        v = 'VOTO NEGADO'
        return f'Com {idade} anos: {v}.'
    elif idade >= 65 or 16 <= idade < 18:
        v = 'VOTO OPCIONAL'
        return f'Com {idade} anos: {v}.'
    else:
        v = 'VOTO OBRIGATÓRIO'
        return f'Com {idade} anos: {v}.'


print('-' * 40)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))