#Escreva um programa que peça a Nota 1 (N1) e a Nota 2 (N2) de 10 alunos e a cada aluno
#mostre a média M, onde M=(N1+N2)/2.

a = 1
while a <= 10:
    n1 = float(input('Insira sua Nota 1: '))
    n2 = float(input('Insira sua Nota 2: '))
    m = (n1 + n2) / 2
    print(f'Sua média foi de {m}')
    a += 1
