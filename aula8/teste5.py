#Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50)
#armazenando em uma lista e uma opção. Se a opção for 1, mostrar o vetor na ordem
#direta, se a opção for 2, mostrar o vetor na ordem inversa.

from random import randint
L = []
op = int(input("1 ou 2: "))
for i in range(10):
    L.append(randint(1,50))
print(L)
if op == 1:
        print(*L)
elif op == 2:
    for i in range(9, -1, -1):
        print(L[i], end=' ')

