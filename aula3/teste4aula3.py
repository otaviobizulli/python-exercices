print('Insira o valor de 3 lados de um triangulo: ')
a = float(input('Valor 1: '))
b = float(input('Valor 2: '))
c = float(input('Valor 3: '))
if a + b < c or a + c < b or b + c < a:
    print('Os valores não formam um triangulo.')
elif a == b == c:
    print('Triangulo Equilatero.')
elif a == b or a == c or a == b:
    print('Triangulo Isosceles.')
elif a != b != c:
    print('Triangulo Escaleno.')
