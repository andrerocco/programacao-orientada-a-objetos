# Exercício 1

lista_notas = []

for i in range(3):
    nota = float(input("Digite a nota {} - ".format(i+1)))
    if nota > 10 or nota < 0:
        print("Nota inválida. Insira uma nota entre 10 e 0.")
        nota = float(input("Digite a nota {} - ".format(i+1)))
    lista_notas.append(nota)

total = 0
for i in lista_notas:
    total += i
media_notas = total / 3
maior_nota = max(lista_notas)
menor_nota = min(lista_notas)
dif_maior_menor = maior_nota - menor_nota

print("\nMédia = {:.2f}".format(media_notas))
print("Maior nota = {:.2f}".format(maior_nota))
print("Menor nota = {:.2f}".format(menor_nota))
print("Diferença entre maior e menor nota = {:.2f}".format(dif_maior_menor))

# Exercício 2

n = int(input("Digite o número de elementos a ser digitado: "))

lista_numeros = []
for i in range(n):
    numero = int(input("Digite um número - ".format(n+1)))
    lista_numeros.append(numero)

lista_numeros.sort()

anterior = None
repetidos = 0
for i in lista_numeros:
    if anterior == i:
        repetidos += 1
    anterior = i

if repetidos != 0:
    print("Existem números repetidos nos números inseridos")
else:
    print("Não existem números repetidos dentro os números inseridos")

# Exercício 3

tupla_qualquer = (47, 6, 123, 32, 54, 90, 928, 20, 9, 101)
maior = 0
menor = 999999
for i in tupla_qualquer:
    if i > maior:
        maior = i
    if i < menor:
        menor = i   
print(maior)
print(menor)

# Exercício 4

lista = (str(input("Insira os valores (serparados por espaço): "))).split()
mult = int(input("Valor que irá multiplicar os números inseridos: "))

lista_multiplicada = []
for i in lista:
    lista_multiplicada.append(int(i)*mult)

print("\nOs valores inseridos multiplicados por {} resultam em:".format(mult))
print(lista_multiplicada)

# Exercício 5

lista_original = []
for i in range(19):
    elemento = int(input("Insira o {}/19 número da lista: ".format(i+1)))
    lista_original.append(elemento)

nova_lista = lista_original[:]

for i in range(9):
    nova_lista[i] = lista_original[18-i]
    nova_lista[18-i] = lista_original[i]

print("A lista: {} \nAgora é: {}".format(lista_original, nova_lista))

# Exercício 6

nome = str(input("Atleta: "))

s1 = float(input("\nPrimeiro salto: "))
s2 = float(input("Segundo salto: "))
s3 = float(input("Terceiro salto: "))
s4 = float(input("Quarto salto: "))
s5 = float(input("Quinto salto: "))

lista = [s1,s2,s3,s4,s5]
lista.sort()
print("\nMelhor salto: {:.1f} m".format(lista[0]))
print("Pior salto: {:.1f} m".format(lista[4]))

lista.pop(4)
lista.pop(0)

total = 0
for i in lista:
    total += i
media = total/len(lista)
print("Média dos demais saltos: {:.1f}".format(media))

print("\nResultado final:")
print("{}: {:.1f} m".format(nome, media))