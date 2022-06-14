from random import randint

menor = 100
linha = 0
maior = 0
m = []
for i in range(10):
    m.append([])
    for j in range(10):
        m[i].append(randint(1,99))

for i in range(10):
    for j in range(10):
        print(f'{m[i][j]:2}',end=' ')
    print()

for i in range(10):
    for j in range(10):
        if m[i][j] > maior:
            maior = m[i][j]
            linha = i

for i in range(10):
    if m[linha][i] < menor:
        menor = m[linha][i]
print(f'o minimax é {menor}, com o maior sendo {maior} na linha {linha+1}.')






