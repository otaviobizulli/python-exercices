#Faça um programa em Python que gere 20 números aleatórios (entre 1 e 50),
#armazene-os em uma lista. Imprima os números e calcule a média apenas dos
#números pares.

from random import randint
L = []
soma = 0
par = 0
for i in range(20):
    L.append(randint(1,50))
    if L[i] % 2 == 0:
        soma += L[i]
        par += 1
media = soma / par
print(L)
print(f'A média dos números pares é {media:.2f}.')