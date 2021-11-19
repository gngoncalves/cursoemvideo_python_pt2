primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))
n = 1
while n <= 10:
    termo = primeiro_termo + (n - 1) * razao
    print(termo, end= ' >> ')
    n += 1
print('Finalizado')