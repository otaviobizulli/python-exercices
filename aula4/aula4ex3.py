print('Insira dois números: ')
N1 = int(input('Primeiro número: '))
N2 = int(input('Segundo número: '))
DIF1 = N1 - N2
DIF2 = N2 - N1
if N1 == N2:
    print('Os números são iguais.')
elif N1 > N2:
    print(f'{N1} é o maior número por uma diferença de {DIF1}.')
else:
    print(f'{N2} é o maior número por uma diferença de {DIF2}.')