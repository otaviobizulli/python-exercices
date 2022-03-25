preco = float(input('Insira o preço do combustivel: '))
kml = float(input('Insira o km/l: '))
dist = float(input('insira a distancia entra as duas cidades: '))
resol = (dist / kml) * preco
print(f'O valor gasto foi de R${resol}')