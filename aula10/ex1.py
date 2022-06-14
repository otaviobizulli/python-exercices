#Faça  um  programa  em Python que  leia  uma  matriz
#2  x  3  de  inteiros,  imprima  a  matriz  e  a soma de todos os elementos

M = []
soma = 0

for i in range(2):
    M.append([])
    for j in range(3):
        M[i].append(int(input()))
        soma += M[i][j]

for i in range(2):
    for j in range(3):
        print(M[i][j], end=' ')
    print()

print(soma)








