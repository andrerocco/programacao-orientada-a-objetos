# EXERCÍCIO 1

while True:
    sexo = input("Digite seu sexo: ")
    if(sexo == "M" or sexo == "F"):
        break

# EXERCÍCIO 2

from random import randrange
numero = randrange(11)
tentativa = 0
while tentativa != numero:
    tentativa = int(input("Advinhe o número: "))
print("Pimba! O número era {}!".format(numero))

# EXERCÍCIO 3

soma = 0
quantidade = 0
maior = None
menor = None
while True:
    digitado = input("Número: ")
    soma = soma + int(digitado)
    quantidade += 1
    
    if int(digitado) == None:
        maior = digitado
    elif int(digitado) > maior:
        maior = digitado
    if int(digitado) == None:
        menor = digitado
    if int(digitado) < menor:
        menor = digitado

    if digitado == "stop":
        break

media = soma / quantidade
print("A média dos {} valores é {}.".format(quantidade, media))
print("O maior valor digitado foi {}. O menor valor digitado foi {}".format(maior, menor))

# EXERCÍCIO 4

while True:
    comando = input("Digite o salário (ou 'stop' para parar): R$ ")
    
    if(comando == "stop"):
        break
    elif (int(comando)*0.11) > 320: 
        salario_desconto = int(comando) - 320
        desconto = 1-(salario_desconto / int(comando))
        print("O desconto foi de R$ 320.00, {:.2%} do valor do salário. O salário com desconto ficou R$ {:.2f}".format(desconto, salario_desconto))
    else:
        salario_desconto = int(comando) * 0.89
        desconto = 1-(salario_desconto / int(comando))
        print("O salário com desconto ficou R$ {:.2f}".format(salario_desconto, desconto))

# EXERCÍCIO 5

numero = int(input("Digite o número de praias que deseja cadastrar: "))
contador = 0
praias_15_20 = 0
soma = 0
mais_dist = ''
maior_dist = 0
while contador < numero:
    nome = str(input("Digite o nome da praia: "))
    dist = float(input("Digite a distância da praia do centro da cidade: "))
    
    if (dist > maior_dist):
        mais_dist = nome
        maior_dist = dist
    
    if (dist >= 15 and dist <= 20):
        praias_15_20 += 1
    
    soma = soma + dist
    contador += 1

media = soma / numero

print("A praia mais distante do centro da cidade é a {} e fica a {}km".format(mais_dist, maior_dist))
print("{} praias estão entre 15km e 20km do centro da cidade".format(praias_15_20))
print("A distância média das praias do centro da cidade é {:.2f}km".format(media))

# EXERCÍCIO FIBONACCI

quantidade = int(input("Digite a quantidade de termos da sua sequência de Fibonacci - "))
contador = 0
a = 0
b = 1
c = 0

while contador < quantidade:
    if contador == (quantidade-1):
        print(c) # Para que não imprima um "-" depois do último termo
        break
    print(c, end=" - ")
    a = b + c
    b = c
    c = a
    contador += 1