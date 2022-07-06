# 1048

def reajuste(salario, percentual):
    salario_reajustado = salario * (1+percentual)
    print("Novo salario: {:.2f}".format(salario_reajustado))
    print("Reajuste ganho: {:.2f}".format(salario_reajustado - salario))
    print("Em percentual: {} %".format(int(percentual*100)))

entrada = float(input())
if entrada > 2000:
    reajuste(entrada, 0.04)
elif entrada > 1200:
    reajuste(entrada, 0.07)
elif entrada > 800:
    reajuste(entrada, 0.10)
elif entrada > 400:
    reajuste(entrada, 0.12)
elif entrada >= 0:
    reajuste(entrada, 0.15)

# 2057

def calcular_tempo(saida, tempo, fuso):
    total = saida + tempo + fuso
    if total == 24:
        total = 0
    elif total > 24 or total < 0:
        total = total % 24
    print(total)

entrada = (str(input())).split()
s = int(entrada[0])
t = int(entrada[1])
f = int(entrada[2])
calcular_tempo(s, t, f)

# 1150

def calcular(x, z):
    total = 0
    contador = 1
    while True:
        total += x
        if total >= z:
            break 
        x+=1
        contador += 1
    print(contador)

x = int(input())
while True:
    z = int(input())
    if x<z:
        calcular(x, z)
        break

# 1154

def calcular_media(soma, contador):
    media = soma / contador
    print("{:.2f}".format(media))

soma = 0
contador = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    contador += 1
    soma += idade

calcular_media(soma, contador)

# 1064

def printar(positivos, soma):
    media = soma / positivos
    print("{} valores positivos".format(positivos))
    print("{}".format(media))

positivos = 0
soma = 0

for i in range(0,6):
    x = float(input())
    if x>0:
        positivos += 1
        soma += x
printar(positivos, soma)

# 1115

def print_quadrante(x, y):
    if x>0 and y>0:
        print("primeiro")
    elif x<0 and y>0:
        print("segundo")
    elif x<0 and y<0:
        print("terceiro")
    elif x>0 and y<0:
        print("quarto")

while True:
    entrada = (str(input())).split()
    x = float(entrada[0])
    y = float(entrada[1])
    
    if x == 0 or y == 0:
        break
    print_quadrante(x, y)

# 2378

def conferir_status_elevador(valor):
    if contador>0:
        print("S")
    else:
        print("N")

dados = (str(input())).split()
n = int(dados[0])
c = int(dados[1])

total = 0
contador = 0
for i in range(0, n):
    info = (str(input())).split()
    s = int(info[0])
    e = int(info[1])
    
    total += (e - s)
    if total > c:
        contador += 1
conferir_status_elevador(contador)

# 2409

def testar(x1, x2, x3):
    if x1>x2 and x1>x3:
        maior = x1
        if x2>x3:
            menor = x3
            meio = x2
        else:
            menor = x2
            meio = x3
    elif x2>x1 and x2>x3:
        maior = x2
        if x1>x3:
            menor = x3
            meio = x1
        else:
            menor = x1
            meio = x3
    elif x3>x1 and x3>x2:
        maior = x3
        if x1>x2:
            menor = x2
            meio = x1
        else:
            menor = x1
            meio = x2
    #Ordena os valores

    if meio <= altura_porta and menor <= largura_porta:
        return True
    elif menor <= altura_porta and meio <= largura_porta:
        return True
    else:
        return False

dimensoes_colchao = (str(input())).split()
c1 = int(dimensoes_colchao[0])
c2 = int(dimensoes_colchao[1])
c3 = int(dimensoes_colchao[2])

dimensoes_porta = (str(input())).split()
altura_porta = int(dimensoes_porta[0])
largura_porta = int(dimensoes_porta[1])

if testar(c1,c2,c3) == True:
    print("S")
elif testar(c1,c2,c3) == False:
    print("N")

# Exercício RETURN 2

def media(soma_notas):
    media = soma_notas / 5
    return media

def status(nota):
    if nota >= 5.75:
        return "APROVADO"
    elif nota >= 2.75:
        return "EM RECUPERAÇÃO"
    else:
        return "REPROVADO"

soma_notas = 0
maior_nota = 0
for i in range(0, 5):
    nota = float(input())
    if nota > maior_nota:
        maior_nota = nota
    soma_notas += nota

print("Média da turma: {:.2f}".format(media(soma_notas)))
print("Maior nota: {:.2f} - Resultado: {}".format(maior_nota, status(maior_nota)))

# Exercício RETURN 3

def paridade(numero):
    if numero % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"

pares = 0
impares = 0

for i in range(10):
    n = int(input())
    print(paridade(n))
    if paridade(n) == "PAR":
        pares += 1
    else:
        impares += 1
print("{} pares e {} ímpares".format(pares, impares))

# Exercício RETURN 4

def primos(x, y):
    for numero in range(x, y+1):
        multiplos = 0        
        for contador in range(2, numero):
            if numero % contador == 0:
                multiplos += 1
        if multiplos == 0:
            print(numero)

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(f"Os números primos no intervalo {n2} - {n1} são: ")
    primos(n2, n1)
elif n2 > n1:
    print(f"Os números primos no intervalo {n1} - {n2} são: ")
    primos(n1, n2)