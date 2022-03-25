#10. Faça um programa para ler 2 valores, calcular e escrever a soma dos inteiros existentes
#entre os 2 valores lidos (incluindo os valores lidos na soma). O programa deve validar que o
#1º valor informado seja menor que o 2º valor. O programa deve permitir que o usuário
#possa executá-lo novamente.
resp = 'S'
som = 0
val = 0
while resp == 'S':
    v1 = int(input("Insira um numero: "))
    v2 = int(input("Insira outro numero: "))
    if v1 > v2:
        print('O primeiro valor deve ser menor que o segundo.')
    else:
        while val < v2:
            val += v1
            som += val
    print(f'A soma do intervalo é de {som}')
    resp = input('Gostaria de inserir outros números [S/N]? ').upper()[0]


