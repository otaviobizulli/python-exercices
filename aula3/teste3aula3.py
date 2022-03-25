rt = (input('Insira R para Retangulo e T para Triangulo: ')).upper()[0]
base = float(input('Insira o valor da base: '))
altura = float(input('Insira o valor da altura: '))
tri = (base * altura)/2
ret = base * altura
if rt == 'R':
    print(f'A area do retângulo é igual a {ret}.')
else:
    print(f'A area do triângulo é igual a {tri}.')
