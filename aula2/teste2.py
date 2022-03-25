print('Digite 3 números: ')
n1 = float(input('Digite o primero número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('O primeiro número é o maior deles!')
if n2 > n1 and n2 > n3:
    print('O segundo número é o maior deles!')
if n3 > n1 and n3 > n2:
    print('O terceiro número é o maior deles!')