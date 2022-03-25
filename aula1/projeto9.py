kmperco = float(input('insira os KM percorridos por voce com o carro alugado: '))
diasalugado = float(input('por quantos dias voce alugou o carro: '))
convdias = diasalugado * 60
convkm = kmperco * 0.15
soma = convdias + convkm
print(f'O valor a pagar será de R${soma:.2f}.')
