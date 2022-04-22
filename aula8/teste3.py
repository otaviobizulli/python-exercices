#Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50),
#armazene-os em uma lista. Imprima os números e imprima todos os números
#múltiplos de 5.

from random import randint
L = []
cinco = []

for i in range(20):
    L.append(randint(1,50))
    if L[i] % 5 == 0:
        cinco.append(L[i])
print(L)
print(cinco)
