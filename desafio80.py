lista = []
for i in range(0, 5):
    num = int(input(f'Insira um número [{i+1}/5]: '))
    if i == 0:
        lista.append(num)
    elif i == 1:
        if num > lista[0]:
            lista.append(num)
        else:
            lista.insert(0, num)
    elif i == 2:
        if num <= lista[0]:
            lista.insert(0, num)
        elif num >= lista[1]:
            lista.append(num)
        elif lista[0] <= num <= lista[1]:
            lista.insert(1, num)
    elif i == 3:
        if num <= lista[0]:
            lista.insert(0, num)
        elif num >= lista[2]:
            lista.append(num)
        elif lista[0] <= num <= lista[1]:
            lista.insert(1,num)
        elif lista[1] <= num <= lista[2]:
            lista.insert(2,num)
    else:
        if num <= lista [0]:
            lista.insert(0, num)
        elif num >= lista[3]:
            lista.append(num)
        elif lista[0] <= num <= lista[1]:
            lista.insert(1, num)
        elif lista[1] <= num <= lista[2]:
            lista.insert(2, num)
        elif lista[2] <= num <= lista[3]:
            lista.insert(3, num)
print(f'A lista inserida e ordenada é: {lista}.')