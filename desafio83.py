eq = list(str(input('Insira a sua equação: ')).strip())
lista = []
for i in eq:
    if i == '(':
        lista.append('(')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')