#Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50),
#armazene-os em uma lista. Imprima os números e imprima todos os números
#múltiplos de um número digitado pelo usuário.

from random import randint
L = []
Mnum = []
num = int(input('num'))
for i in range(20):
    L.append(randint(1,50))
    if L[i] % num == 0:
        Mnum.append(L[i])
print(L)
print(Mnum)


