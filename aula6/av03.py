n = int(input('Insira o numero que quer saber da tabuada: '))

if n > 0:
    for i in range(1, n + 1):
        for j in range(i, i * n + 1, i):
            print(j,end=' ')
        print()
else:
    print('ERRO. Insira um número maior que zero.')
