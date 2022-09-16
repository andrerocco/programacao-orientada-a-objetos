idades = []
alturas = []

for i in range(5):
    idades.append(int(input("Digite a idade: ")))
    alturas.append(float(input("Digite a altura: ")))

print("Idades: {}".format(", ".join([str(x) for x in idades[::-1]])))
print("Alturas: {}".format(", ".join([str(x) for x in alturas[::-1]])))
