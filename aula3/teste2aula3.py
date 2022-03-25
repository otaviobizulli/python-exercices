placa = int(input('Insira apenas a parte numerica da placa: '))
if placa > 9999 or placa < 1000:
    print('Placa Inválida.')
else:
    pn = placa % 10
    if pn == 1 or pn == 2:
        print('Segunda-feira')
    elif pn == 3 or pn == 4:
        print ('Terça-feira.')
    elif pn == 5 or pn == 6:
        print ('Quarta-feira.')
    elif pn == 7 or pn == 8:
        print('Quinta-feira.')
    else:
        print('Sexta-feira.')

