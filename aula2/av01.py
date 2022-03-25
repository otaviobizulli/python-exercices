x1 = float(input('Insira x1 do plano: '))
x2 = float(input('Insira x2 do plano: '))
y1 = float(input('Insira y1 do plano: '))
y2 = float(input('Insira y2 do plano: '))
dist = (((x2 - x1) **2) + ((y2 - y1) **2)) **0.5
print(f'O valor da distancia é de {dist:.4f}.')