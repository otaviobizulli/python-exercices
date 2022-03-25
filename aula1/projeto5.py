dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

convdias = (((dias * 24) * 60) * 60)
convhoras = ((horas * 60) * 60)
convmin = minutos * 60

soma = convdias + convhoras + convmin + segundos

print(f"O total em segundos é de {soma}.")