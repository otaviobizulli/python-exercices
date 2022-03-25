print('Digite 3 números inteiros diferentes: ')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))
if n1 > n2 > n3:
    print(f'Ordem Crescente: {n3}; {n2}; {n1}.')
elif n1 > n3 > n2:
    print(f'Ordem Crescente: {n2}; {n3}; {n1}.')
elif n2 > n1 > n3:
    print(f'Ordem Crescente: {n3}; {n1}; {n2}.')
elif n2 > n3 > n1:
    print(f'Ordem Crescente: {n1}; {n3}; {n2}.')
elif n3 > n2 > n1:
    print(f'Ordem Crescente: {n1}; {n2}; {n3}.')
elif n3 > n1 > n2:
    print(f'Ordem Crescente: {n2}; {n1}; {n3}.')



