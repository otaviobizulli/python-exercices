SAL = float(input('Insira seu salário: '))
PREST = float(input('Insira o valor da prestação: '))
PORC = SAL * (20/100)

if PREST > PORC:
    print('Empréstimo não concedido.')
else:
    print('Empréstimo concedido.')