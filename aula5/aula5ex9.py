#9. Elabore um programa para mostrar a sequência dos N primeiro números da série de Fibonacci:
#1 1 2 3 5 8 13 21 34 55 89 ....
#Sempre o próximo elemento é a soma dos dois anteriores, assim, no exemplo o próximo é 144.

ult = 0
num = 1
while num <= 144:
    print(num)
    ult, num = num, ult
    num += ult

