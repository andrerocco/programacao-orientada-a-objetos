# 1437

while True:
    num = int(input())
    if num == 0:
        break
    comandos = str(input())

    direcao = 0
    for i in range(num):
        virar = comandos[i]
        if virar == "D":
            direcao += 1
        elif virar == "E":
            direcao -= 1
    
    direcao = direcao % 4
    
    if direcao == 0:
        print("N")
    elif direcao == 1:
        print("L")
    elif direcao == 2:
        print("S")
    elif direcao == 3:
        print("O")

# 2813

n = int(input())

para_casa, para_trabalho = 0, 0
na_casa, no_trabalho = 0, 0

for i in range(n):
    entrada_dia, entrada_noite = [str(i) for i in input().split()]
    
    if entrada_dia == "chuva" and para_casa == 0 and na_casa == 0:
        para_casa += 1
        no_trabalho += 1
    elif entrada_dia == "chuva" and na_casa != 0:
        na_casa -= 1
        no_trabalho += 1
    elif entrada_dia == "chuva" and na_casa == 0:
        para_casa += 1
        no_trabalho += 1
    if entrada_noite == "chuva" and no_trabalho == 0:
        para_trabalho += 1
        na_casa += 1
    elif entrada_noite == "chuva" and no_trabalho != 0:
        no_trabalho -= 1
        na_casa += 1

print("{} {}".format(para_casa, para_trabalho))

# 1192

n = int(input())

for i in range(n):
    entrada = str(input())
    e1 = int(entrada[0])
    e2 = entrada[1]
    e3 = int(entrada[2])
    
    if e1 == e3:
        print(e1*e3)
    elif e2.islower() == True:
        print(e1+e3)
    elif e2.isupper() == True:
        print(e3-e1)

# 1168

def leds(inteiro):
    total = 0
    for i in range(len(inteiro)):
        n = int(inteiro[i])
        if n == 0:
            total += 6
        elif n == 1:
            total += 2
        elif n == 2:
            total += 5
        elif n == 3:
            total += 5
        elif n == 4:
            total += 4
        elif n == 5:
            total += 5
        elif n == 6:
            total += 6
        elif n == 7:
            total += 3
        elif n == 8:
            total += 7
        elif n == 9:
            total += 6
    return total

n = int(input())

for i in range(n):
    inteiro = str(input())
    numero_leds = leds(inteiro)
    print("{} leds".format(numero_leds))

# 1094

n = int(input())

c = 0
r = 0
s = 0
total = 0

for i in range(n):
    entrada = (str(input())).split()
    quantidade = int(entrada[0])
    tipo = entrada[1]
    
    total += quantidade
    
    if tipo == 'C':
        c += quantidade
    elif tipo == 'R':
        r += quantidade
    elif tipo == 'S':
        s += quantidade
        
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(c))
print("Total de ratos: {}".format(r))
print("Total de sapos: {}".format(s))

p_c = (c / total)*100
p_r = (r / total)*100
p_s = (s / total)*100
print("Percentual de coelhos: {:.2f} %".format(p_c))
print("Percentual de ratos: {:.2f} %".format(p_r))
print("Percentual de sapos: {:.2f} %".format(p_s))

# Exercício 6

while True:
    lenght, entrada = [str(i) for i in input().split()]
    
    if int(lenght) == 0:
        break
    
    soma = 0
    for i in range(int(lenght)):
        soma += int(entrada[i])

    if soma%3 == 0:
        print("{} sim".format(soma))
    else:
        print("{} não".format(soma))