#Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) sem
#números repetidos. Imprima o vetor

from random import sample


L = list(range(1,50))
M = sample(L,10)
print(M)

