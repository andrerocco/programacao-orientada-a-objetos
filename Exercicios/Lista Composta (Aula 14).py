# Exemplo 1

lista_pessoas = []
lista_temporaria = []

while True:
    print("Digite 0 para parar de cadastrar")
    nome = str(input("Nome: "))
    if nome == '0':
        break
    peso = float(input("Peso: "))
    if peso == 0:
        break
    
    lista_temporaria.append(nome)
    lista_temporaria.append(peso)
    
    if len(lista_pessoas) == 0:
        maior = menor = lista_temporaria[:]
    else:
        if lista_temporaria[1] > maior[1]:
            maior = lista_temporaria[:]
        if lista_temporaria[1] < menor[1]:
            menor = lista_temporaria[:]
            
    
    lista_pessoas.append(lista_temporaria[:])
    lista_temporaria.clear()

print("\nNúmero de pessoas cadastradas: {}".format(len(lista_pessoas)))
print("Maior peso cadastrado: {} kg".format(maior[1]))
print("Menor peso cadastrado: {} kg".format(menor[1]))

# Exemplo 2

lista_composta = []
pares = []
impares = []

lista_composta.append(pares)
lista_composta.append(impares)

for i in range(10):
    num = int(input("Número: "))
    
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort()

print("\nPares:")
for i in pares:
    print(i)
    
print("\nÍmpares")
for i in impares:
    print(i)

# Exercício 1

matriz = []
maior_20_anos = []
lista_mais_pesados = []
lista_mais_leves = []

while True:
    lista_temporaria = []
    lista_temporaria.append(str(input("Nome: ")))
    idade = int(input("Idade: "))
    lista_temporaria.append(idade)
    lista_temporaria.append(float(input("Peso: ")))
    
    if idade >= 20:
        maior_20_anos.append(lista_temporaria)
    
    if len(matriz) == 0:
        mais_pesada = mais_leve = lista_temporaria[:]
        lista_mais_pesados.append(lista_temporaria[:])
        lista_mais_leves.append(lista_temporaria[:])
    else:
        if lista_temporaria[2] > mais_pesada [2]:
            lista_mais_pesados.clear()
            mais_pesada = lista_temporaria[:]
            lista_mais_pesados.append(lista_temporaria[:])
        elif lista_temporaria[2] == mais_pesada [2]:
            lista_mais_pesados.append(lista_temporaria[:])
        
        if lista_temporaria[2] < mais_leve [2]:
            lista_mais_leves.clear()
            mais_leve = lista_temporaria[:]
            lista_mais_leves.append(lista_temporaria[:])
        elif lista_temporaria[2] == mais_leve [2]:
            lista_mais_leves.append(lista_temporaria[:])
    
    matriz.append(lista_temporaria)
    
    continuar = str(input("CONTINUAR CADASTRANDO? [S/N] ")).lower()
    if continuar != "s":
        break
    
print("\n------- ESTATÍSTICAS -------")
print("{} pessoas foram cadastradas".format(len(matriz)))

print("\nPessoas mais pesadas: ".format(lista_mais_pesados))
for i in lista_mais_pesados:
    print("{} - {}kg".format(i[0], i[2]))

print("\nPessoas mais leves: ".format(lista_mais_leves))
for i in lista_mais_leves:
    print("{} - {}kg".format(i[0], i[2]))

print("\n{} pessoas com 20 anos ou mais:".format(len(maior_20_anos)))
for i in maior_20_anos:
    print("{} - {} anos - {}kg".format(i[0], i[1], i[2]))

# 1181

linha_escolhida = int(input())
operacao_escolhida = str(input())

matriz = []
for x in range(12):
    matriz.append([])

for l in range(12):
    for c in range(12):
        matriz[l].append(float(input()))

soma = 0
for elemento in matriz[linha_escolhida]:
    soma += elemento

if operacao_escolhida == "S":
    print(soma)
elif operacao_escolhida == "M":
    print(soma/12)

# 1184

operacao_escolhida = str(input())

matriz = []
for x in range(12):
    matriz.append([])

for l in range(12):
    for c in range(12):
        matriz[l].append(float(input()))

soma = 0
contador = 0
for i in range(1, 12):
    for j in range(i):
        soma += matriz[i][j]
        contador += 1

if operacao_escolhida == "S":
    print("{:.1f}".format(soma))
elif operacao_escolhida == "M":
    print("{:.1f}".format(soma/contador))

# 1796

participantes = int(input())
resultado = str(input()).split()

positivo = 0
negativo = 0
for i in range(participantes):
    if int(resultado[i]) == 1:
        positivo += 1
    elif int(resultado[i]) == 0:
        negativo += 1

if positivo > negativo:
    print("Y")
else:
    print("N")
