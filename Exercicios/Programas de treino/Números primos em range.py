def primos(x, y):
    for numero in range(x, y+1):
        multiplos = 0        
        for contador in range(2, numero):
            if numero % contador == 0:
                multiplos += 1
        if multiplos == 0:
            print(numero)

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(f"Os números primos no intervalo {n2} - {n1} são: ")
    primos(n2, n1)
elif n2 > n1:
    print(f"Os números primos no intervalo {n1} - {n2} são: ")
    primos(n1, n2)
