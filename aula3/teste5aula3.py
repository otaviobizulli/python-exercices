print('Insira o valor de 3 angulos de um triangulo: ')
a1 = float(input('Valor 1: '))
a2 = float(input('Valor 2: '))
a3 = float(input('Valor 3: '))
if a1 + a2 + a3 != 180:
    print('Os valores não formam um triangulo. "A soma dos angulos internos de um triangulo sempre é igual a 180."')
elif a1 == 90 or a2 == 90 or a3 == 90:
    print('Triângulo Retângulo.')
elif a1 > 90 or a2 > 90 or a3 > 90:
    print('Triângulo Obtusângulo.')
elif a1 < 90 and a2 < 90 and a3 < 90:
    print('Triângulo Acutângulo.')