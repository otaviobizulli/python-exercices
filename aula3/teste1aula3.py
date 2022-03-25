num = int(input('Insira um número de 3 algarismos: '))
c = num // 100
d = num % 100 // 10
u = num % 10
if num <= 99 or num >= 1000:
    print('Numero Inválido.')
elif c < d < u:
    print('Seu número é ascendente!')
else:
    print('Seu número não é ascendente!')

