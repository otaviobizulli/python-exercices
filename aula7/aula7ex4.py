p = int(input())
d1 = int(input())
d2 = int(input())

if (p == 0):
    if (d1 + d2)%2 == 0:
        print(0)
    else:
        print(1)
else:
    if (d1 + d2)%2 == 1:
        print(0)
    else:
        print(1)
