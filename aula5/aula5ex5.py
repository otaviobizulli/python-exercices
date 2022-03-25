#5. Escreva um programa para ler 10 números do usuário e calcular a soma dos números pares
#e a soma dos números ímpares.

n = 1
sp = 0
si = 0
while n <= 10:
    num = int(input('Insira um número: '))
    if num%2 == 0:
        sp += num
    else:
        si += num
    n += 1
print(f'A soma dos números pares é de {sp} e a soma dos impares é de {si}.')