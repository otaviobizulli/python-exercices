#Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50)
#armazenando na lista A e um valor x. Criar o vetor B contendo os elementos do vetor
#A multiplicados por x. Imprima os dois vetores.

from random import randint
LA = []
LB = []
for i in range(10):
    LA.append(randint(1,50))
print(*LA)
X = int(input('X: '))
for i in range(10):
    LB.append(LA[i] * X)
print(*LB)


