#3. Escreva um programa que peça um nome e o imprima 10 vezes.

nome = input('Insira o seu nome: ')
n = 1
while n <= 10:
    print(f'{n} {nome}',end=' ')
    n += 1
