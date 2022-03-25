N1 = int(input('Insira um número: '))
N2 = int(input('Insira outro número: '))
v = 0
cent1 = N1 // 100
dez1 = (N1 % 100) // 10
uni1 = N1 % 10
cent2 = N2 // 100
dez2 = (N2 % 100) // 10
uni2 = N2 % 10
if (uni1 + uni2) >= 10:
    v += 1
    dez1 += 1
if (dez1 + dez2) >= 10:
    v += 1
    cent1 += 1
if (cent1 + cent2) >= 10:
    v += 1
print(f'total de {v} "vai 1"')

