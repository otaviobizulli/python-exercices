salario = float(input('insira seu salario: '))
reajus = float(input('insira seu percentual de reajuste: '))
resol = salario * (reajus / 100)
resol2 = salario + resol
print(f'seu novo salario sera de R${resol2}.')