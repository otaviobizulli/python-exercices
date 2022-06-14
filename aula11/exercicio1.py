from random import randint

al = 1

g = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
r = ['a', 'b', 'c', 'd', 'e']
m = []
for i in range(5):
    m.append([])
    cont = 0
    for j in range(10):
        m[i].append(r[randint(0,4)])
    print()

for i in range(5):
    cont = 0
    for j in range(10):
        if m[i][j] == g[j]:
            cont += 1
    print(f'o aluno {al}, acertou {cont} questoes.')
    al += 1
