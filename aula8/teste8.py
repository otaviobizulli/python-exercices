# Faça um programa em Python que gere 20 elementos aleatórios (entre 1 e 50)
#armazenando no vetor A e crie outros 2 vetores B e C. O vetor B deve ter apenas os
#números pares e o vetor C deve conter apenas os números ímpares. Imprima os três
#vetores.

from random import randint
LA = []
LB = []
LC = []
for i in range(20):
    LA.append(randint(1,50))
    if LA[i] % 2 == 0:
        LB.append(LA[i])
    else:
        LC.append(LA[i])
print(*LA)
print(*LB)
print(*LC)
