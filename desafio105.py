def notas(*turma, sit=False):
    """
    Função para analisar notas de uma turma.
    :param turma: notas de uma turma de alunos.
    :param sit: Verifica a  situação da turma.
    :return: dicionário com informações analisadas da turma.
    """
    sala = {}
    sala['Total'] = len(turma)
    sala['Maior'] = max(turma)
    sala['Menor'] = min(turma)
    sala['Média'] = sum(turma)/len(turma)
    if sit:
        if sala['Média'] >= 7:
            sala['Situação'] = 'BOA'
        elif 5 <= sala['Média'] < 7:
            sala['Situação'] = 'RAZOÁVEL'
        else:
            sala['Situação'] = 'RUIM'
    return sala


classe = notas(8,9)
print(classe)