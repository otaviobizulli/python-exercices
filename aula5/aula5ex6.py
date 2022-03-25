#.Igual ao exercício anterior, mas pedir antes do laço a quantidade de números a serem lidos

n = 1
sp = 0
si = 0
sl = int(input('Quantidade de numeros a serem lidos: '))
while n <= sl:
    num = int(input('Insira um número: '))
    if num%2 == 0:
        sp += num
    else:
        si += num
    n += 1
print(f'A soma dos números pares é de {sp} e a soma dos impares é de {si}.')