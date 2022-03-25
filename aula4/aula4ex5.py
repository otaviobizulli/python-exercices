LAB = float(input('Insira sua nota de laboratório: '))
SEM = float(input('Insira sua nota da avaliação semestral: '))
FIN = float(input('Insira sua nota da avaliação final: '))
RES = ((LAB * 2) + (SEM * 3) + (FIN * 5)) / 10

if LAB < 0 or LAB > 10:
    print('As notas vão de 0 a 10.')
elif SEM < 0 or SEM > 10:
    print('As notas vão de 0 a 10.')
elif FIN < 0 or FIN > 10:
    print('As notas vão de 0 a 10.')

elif RES >= 0 and RES <= 2.9:
    print(f'Reprovado com uma média de {RES}.')
elif RES >= 3 and RES <= 4.9:
    print(f'Recuperação com uma média de {RES}.')
else:
    print(f'Aprovado com uma média de {RES}.')