#Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e
#ordene os números em ordem ascendente. Imprima o vetor antes e após a ordenação.
#Pesquise sobre os métodos de ordenação

from random import randint
L = []
for i in range(10):
    L.append(randint(1,50))
print(L)
L.sort(reverse = False)
print(L)