#Faça  um  programa  que gere dois  conjuntos  de números  inteiros  distintos  e  imprima
#a interseção  destes  dois  conjuntos  (os  números  presentes  em  ambos  os  conjuntos).
#Exemplo:
#Primeiro conjunto: 1 2 3 4 5
#Segundo conjunto: 2 5 7 1 9 18
#Resultado: 1 2 5

from random import sample

O = []
L = list(range(1,20))
M = sample(L, 5)
N = sample(L, 5)
print(M)
print(N)

for i in range(5):
    if M[i] in N:
        O.append(M[i])

print(O)