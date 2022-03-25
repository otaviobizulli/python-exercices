N1 = int(input('Insira um número positivo: '))

QUAD = N1 ** 2
RAIZ = N1 ** 0.5

if N1 < 0:
    print('Não é um número positivo.')
else:
    print(f'O resultado do seu número ao quadrado será igual a {QUAD}, e o resultado de sua raiz será igual a {RAIZ}.')

