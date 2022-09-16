numeros1 = []
numeros2 = []

for i in range(10):
    numeros1.append(float(input("VETOR1 - Digite um número real: ")))
    numeros2.append(float(input("VETOR2 - Digite um número real: ")))

numeros3 = []

for i in range(10):
    numeros3.append(numeros1[i])
    numeros3.append(numeros2[i])

print("VETOR3: {}".format(numeros3))