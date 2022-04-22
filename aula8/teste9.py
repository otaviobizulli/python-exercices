#Faça um programa em Python que gere 10 elementos aleatórios (entre 1 e 50) e peça
#um número ao usuário. Verifique se este número pertence ou não ao vetor. Imprima
#o vetor e a mensagem de número encontrado ou não.

from random import randint
L = []
num = int(input('Insira um número: '))
for i in range(10):
    L.append(randint(1,50))
if num in L:
    print(f'{num} esta dentro da lista.')
else:
    print(f'{num} não esta dentro da lista.')
print(*L)
