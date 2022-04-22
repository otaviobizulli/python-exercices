#Elabore  um  programa  que  calcule  N!  (fatorial  de  N),
#sendo  que  o  valor  inteiro  de  N  é fornecido pelo usuário.

n = int(input('Insira o valor de N para N!: '))
val = 1
n1 = n

while (n > 1):
    n -= 1
    val = val * n
print(val*n1)


