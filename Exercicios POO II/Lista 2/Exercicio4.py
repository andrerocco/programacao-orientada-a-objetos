print('Digite 10 caracteres')

lista_consoantes = []
for i in range(10):
    letra = str(input(f"{i+1}. Digite a letra: ")).lower()
    if letra not in ['a', 'e', 'i', 'o', 'u']:
        lista_consoantes.append(letra)

print(f"Total de consoantes: {len(lista_consoantes)}")
print("Consoantes:", " ".join(lista_consoantes))