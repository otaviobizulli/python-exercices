#Faça um programa em Python que gere 10 números aleatórios (entre 1 e 50),
#armazene-os em uma lista. Imprima os números e calcule quantos são números pares
#e quantos são números ímpares

from random import randint
L = []
par = 0
impar = 0
for i in range(10):
    L.append(randint(1,50))
    if L[i] % 2 == 0:
        par += 1
    else:
        impar += 1
print(L)
print(f'{par} são pares e {impar} são impares.')




