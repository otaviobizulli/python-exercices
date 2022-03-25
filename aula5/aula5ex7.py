#7. Escreva um programa que gere um conjunto de 20 números inteiros aleatórios entre 1 e 50
#e mostre qual foi o maior e o menor valor gerado.
from random import randint

mavg = 25
mevg = 25
numale = 1
while numale <= 20:
    numale += 1
    ger = randint(1, 50)
    print(f'O número gerado foi {ger}')
    if ger >= mavg:
        mavg, ger = ger, mavg
    elif ger <= mevg:
        mevg, ger = ger, mevg
print(f'O maior número encontrado foi {mavg} e o menor foi {mevg}')


