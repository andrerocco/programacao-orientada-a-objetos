#1003
a = int(input("Número A: "))
b = int(input("Número B: "))
    
soma = a + b
print("SOMA = {}".format(soma))

#1004
a = int(input("Número A: "))
b = int(input("Número B: "))
    
produto = a * b
print("PRODUTO = {}".format(produto))

#1005
a = float(input("Número A: "))
b = float(input("Número B: "))

media = ((a * 3.5) + (b * 7.5)) / 11
print("MEDIA = {:.5f}".format(media))

#1006
a = float(input("Número A: "))
b = float(input("Número B: "))
c = float(input("Número C: "))

media = ((a * 2) + (b * 3) + (c * 5))/10
print("MEDIA = {:.1f}".format(media))

#1007
a = int(input("Número A: "))
b = int(input("Número B: "))
c = int(input("Número C: "))
d = int(input("Número D: "))

diferenca = (a * b - c * d)
print("DIFERENCA  =", diferenca)

#1008
numero_funcionario = int(input("Insira o número do funcionário: "))
numero_horas = int(input("Insira o número de horas trabalhadas: "))
salario_hora = float(input("Insira o salário / hora:  "))

salario = numero_horas * salario_hora

print("NUMBER = {}".format(numero_funcionario))
print("SALARY = U$ {}".format(salario))

#1009
nome = input()
salario = float(input())
vendas = float(input())

total = salario + (vendas*0.15)

print(f"TOTAL = R$ {total:.2f}")

#1012
a = float(input())
b = float(input())
c = float(input())

triangulo = (a*c)/2
circulo = 3.14159*(c*c)
trapezio = ((a+b)*c)/2
quadrado = b*b
retangulo = a*b

print("TRIANGULO: {:.3f}".format(triangulo))
print("CIRCULO: {:.3f}".format(circulo))
print("TRAPEZIO: {:.3f}".format(trapezio))
print("QUADRADO: {:.3f}".format(quadrado))
print("RETANGULO: {:.3f}".format(retangulo))

#1014
distancia = int(float(input()))
combustivel = float(input())

gasto = distancia / combustivel
print("{:.3f} km/l".format(gasto))

#1015
import math
from math import sqrt, pow

p1 = input("Digite as coordenadas de P1 (x1 y1): ")
p2 = input("Digite as coordenadas de P2 (x2 y2): ")

l1 = p1.split()
l2 = p2.split()
x1 = float(l1[0])
y1 = float(l1[1])
x2 = float(l2[0])
y2 = float(l2[1])

distancia = sqrt(pow((x2-x1), 2) + pow(y2-y1, 2))
print("A distância entre os pontos é {:.4f}".format(distancia))

#1017
tempo = int(input("Digite o tempo da viagem em horas: "))
velocidade_media = int(input("Digite a velocidade media da viagem em km/h: "))

distancia = tempo * velocidade_media
litros = distancia / 12
print("Seu gastando 1L a cada 12km, você consumirá {:.3f}L".format(litros))

#1019
x = int(input("Digite o número de segundos a serem convertidos em horas e minutos: "))

segundos = int(x % 60)
minutos = int(x // 60)
horas = 0
if (minutos > 60):
    horas = int(minutos // 60)
    minutos = int(minutos % 60)
print("{}:{}:{}".format(horas, minutos, segundos))

#1020
x = int(input("Digite o número de dias: "))
anos = x // 365
if ((x//365) >= 1):
    dias = x % 365
    dias = dias % 30
    meses = x % 365
    meses = meses // 30
else:
    dias = x % 30
    meses = x // 30
print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))

#2374
pressao_desejada = int(input())
pressao_lida = int(input())

dif = pressao_desejada - pressao_lida
print(dif)

#2413
n3 = int(input())
n1 = (n3*2)*2
print(n1)