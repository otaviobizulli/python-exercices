n = int(input("Insira o número de sushis [1/8]: "))
qnt = (10**n) - 1
L = []

for i in range(qnt, 10*(n-1), -1):
   div = 0
   nn = i
   for j in range(n):
       primo = True
       if nn <= 1:
           primo = False
       else:
           for k in range(2, nn//2 + 1):
               if nn % k == 0:
                   primo = False
                   break
       if primo:
           div += 1
       else:
           break
       nn //= 10
   if n == div:
       L.append(i)

print(L[::-1])