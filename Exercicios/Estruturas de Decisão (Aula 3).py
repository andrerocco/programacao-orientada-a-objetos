#EXERCÍCIO 1

valor_casa = float(input("Valor da casa: "))
salario = float(input("Salário do comprador: "))
anos = float(input("Em quantos anos será paga: "))

meses = anos * 12
prestacao = valor_casa / meses

if(prestacao > (salario * 0.3)):
    print("Empréstimo negado - Valor da prestação excede 30% do salário")
else:
    print("Empréstimo aprovado")
    print("Valor da prestação: R$ {:.3f}".format(prestacao))


#EXERCÍCIO 2

valor_produto = float(input("Insira o valor do produto: R$ "))

print("----------- Formas de pagamento -----------")
print("a. à vista (dinheiro ou cheque) - 10% de desconto ")
print("b. 1x no cartão - 5% de desconto  ")
print("c. 2x no cartão - Preço normal    ")
print("d. 3x ou mais no cartão - 20% de juros    ")
print("\n Digite a letra da opção de pagamento: ")
escolha = str(input("- ")).lower().strip()

print("\n----------- Resultado -----------")
if (escolha == "a"):
    valor_pago = valor_produto * 0.9
    print(f"Valor final à ser pago: R$ {valor_pago} em dinheiro")
elif (escolha == "b"):
    valor_pago = valor_produto * 0.95
    print(f"Valor final à ser pago: R$ {valor_pago}")
    print("1x no cartão")
elif (escolha == "c"):
    valor_pago = valor_produto
    print(f"Valor final à ser pago: R$ {valor_pago}")
    print("2x R$ {} no cartão".format((valor_pago/2)))
elif (escolha == "d"):
    valor_pago = valor_produto * 1.20
    print(f"Valor final à ser pago: R$ {valor_pago}")
    print("3x R$ {} no cartão".format((valor_pago/3)))
else:
    print("Escolha de forma de pagamento inválida")


# EXERCÍCIO 3

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em cm: "))

altura_metro = altura / 100
imc = peso / (altura_metro * altura_metro)
print("Seu IMC é {:.1f}".format(imc))

if (imc < 18.5):
    print("Abaixo do peso")
elif (imc < 25):
    print("Peso ideal")
elif (imc < 30):
    print("Sobrepeso")
elif (imc < 40):
    print("Obesidade")
elif (imc >= 40):
    print("Obesidade mórbida")
    

#EXERCÍCIO 4

a = int(input())
b = int(input())
c = int(input())
d = int(input())

paridade = a % 2
if (b>c and d>a and ((c+d)>(a+b)) and c>=0 and d>=0 and paridade==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


#EXERCÍCIO 5

n = float(input())

if(n>100 or n<0):
    print("Fora de intervalo")
elif(n<=25):
    print("Intervalo [0,25]")
elif(n<=50):
    print("Intervalo (25,50]")
elif(n<=75):
    print("Intervalo (50,75]")
elif(n<=100):
    print("Intervalo (75,100]")


#EXERCÍCIO 6

entrada = str(input())
cod = int(entrada.split()[0])
qnt = int(entrada.split()[1])

if (cod == 1):
    total = float(qnt * 4)
elif (cod == 2):
    total = float(qnt * 4.5)
elif (cod == 3):
    total = float(qnt * 5)
elif (cod == 4):
    total = float(qnt * 2)
elif (cod == 5):
    total = float(qnt * 1.5)

print("Total: R$ {:.2f}".format(total))


#EXERCÍCIO 7

numbers = str(input())
n1 = float(numbers.split()[0])
n2 = float(numbers.split()[1])
n3 = float(numbers.split()[2])
n4 = float(numbers.split()[3])

media = ((n1*2)+(n2*3)+(n3*4)+n4)/10
print("Media: {:.1f}".format(media))

if (media >= 7):
    print("Aluno aprovado.")
    
elif(media >= 5 and media <= 6.9):
    print("Aluno em exame.")
    
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    
    nota_final = (media+exame)/2
    if (nota_final >= 5):
        print("Aluno aprovado.")
    elif(nota_final <= 4.9):
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(nota_final))
    
elif (media < 5):
    print("Aluno reprovado.")


#EXERCÍCIO 8

lados = str(input())
lista_str = lados.split()
lista_lados = sorted([float(x) for x in lista_str])
#Transforma a entrada em lista > Converte cada element para um float > Organiza a lista em ordem decrescente

if (lista_lados[2] < lista_lados[1] + lista_lados[0]):
    perimetro = lista_lados[0]+lista_lados[1]+lista_lados[2]
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((lista_lados[2]+lista_lados[1])*lista_lados[0]) / 2
    print("Area = {:.1f}".format(area))


#EXERCÍCIO 9

valor = input().split()
a = int(valor[0])
b = int(valor[1])
if(a%b == 0):
    print("Sao Multiplos")
elif(b%a == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")


#EXERCÍCIO 10

valores = str(input()).split()
lista = sorted([float(x) for x in valores])

a = lista[2]
b = lista[1]
c = lista[0]

if(a >= b+c):
    print("NAO FORMA TRIANGULO")
if(a*a == b*b + c*c):
    print("TRIANGULO RETANGULO")
if(a*a > b*b + c*c):
    print("TRIANGULO OBTUSANGULO")
if(a*a < b*b + c*c):
    print("TRIANGULO ACUTANGULO")
if(a == b == c):
    print("TRIANGULO EQUILATERO")
if(a == b or a == c or b == c):
    print("TRIANGULO ISOSCELES")


#EXERCÍCIO 11

entrada = str(input()).split()

if(int(entrada[0])*int(entrada[2]) <= int(entrada[1])):
    print("S")
else:
    print("N")


#EXERCÍCIO 12

vertebra = str(input())
classe = str(input())
alimentacao = str(input())

if(vertebra == "vertebrado"):
    if(classe == "ave"):
        if(alimentacao == "carnivoro"):
            print("aguia")
        elif(alimentacao == "onivoro"):
            print("pomba")
    elif(classe == "mamifero"):
        if(alimentacao == "onivoro"):
            print("homem")
        elif(alimentacao == "herbivoro"):
            print("vaca")

elif(vertebra == "invertebrado"):
    if(classe == "inseto"):
        if(alimentacao == "hematofogo"):
            print("pulga")
        elif(alimentacao == "herbivoro"):
            print("lagarta")
    elif(classe == "anelidio"):
        if(alimentacao == "hematofogo"):
            print("sanguessuga")
        elif(alimentacao == "onivoro"):
            print("minhoca")


#EXERCÍCIO 13

import math
from math import sqrt, pow

entrada = str(input()).split()
l = int(entrada[0])
a = int(entrada[1])
p = int(entrada[2])
diam = int(entrada[3]) * 2

diagonal = sqrt(pow(sqrt(a*a+l*l), 2) + p*2)

if(diagonal <= diam):
    print("S")
else:
    print("N")


#EXERCÍCIO 14

nota1 = float(input("Digite a NOTA 1: "))
nota2 = float(input("Digite a NOTA 2: "))
nota3 = float(input("Digite a NOTA 3: "))
media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Em recuperação")
else:
    print("Reprovado")
