from random import sample

cont1 = 16
cont = 1

m = []
for i in range(5):
    for j in range(5):
        m.append(sample(range(cont, cont1), 5))
        cont += 15
        cont1 += 15
    print()

m[2][2] = '🍀'

for i in range(5):
    for j in range(5):
        print(f'{m[j][i]:2}',end=' ',)
    print()


