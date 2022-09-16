numeros = []

for i in range(10):
    numeros.append(float(input("Digite um número real: ")))

soma = 0
for numero in numeros:
    soma += numero**2

print("Soma dos quadrados de cada elemento: {}".format(soma))