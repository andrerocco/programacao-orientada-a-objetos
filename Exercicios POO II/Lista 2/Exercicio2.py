vetor = []
print("Adicione 10 reais para o vetor")
for i in range(10):
    vetor.append(float(input(f"{i+1}. Digite o real: ")))
print(vetor[::-1])