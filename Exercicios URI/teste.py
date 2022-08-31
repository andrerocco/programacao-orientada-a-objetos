from math import sqrt

contador = 0
i = 1

length = 10

while contador < length:
    divisores_numero = 0

    limit = int(sqrt(i))
    for k in range(1, limit+1):
        if (i % k == 0): 
            divisores_numero += 1
            if (k != i/k):
                divisores_numero += 1

    if (divisores_numero == 2):
        print(i)
        contador += 1

    
    i += 1