a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))

if a == 0:
    print('o valor de A deve ser diferente de 0.')

delta = (b ** 2) - (4 * a * c)
rdelta = delta ** 0.5

x1 = (- b + rdelta) / (2 * a)
x2 = (- b - rdelta) / (2 * a)

if delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    print('Raiz única.')
else:
    print(f'As duas raízes reais são {x1} e {x2}.')


