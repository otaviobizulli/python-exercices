#Faça um programa em Python que gere uma matriz 10 x 10 de inteiros aleatórios entre 1 e 50,
#imprima a matriz e a média de todos os elementos.

from random import randint

M = []
soma = 0

for i in range(10):
    M.append([])
    for j in range(10):
        M[i].append(randint(1,50))
        print(f'{M[i][j]:02}', end=' ')
        soma += M[i][j]
    print()
med = soma / 100

print(med)






