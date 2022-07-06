#1075

n = int(input())

contador = 1
while contador < 10000: 
  resto = contador % n
  if resto == 2:
    print(contador)
  contador += 1
  
#1078

n = int(input())
contador = 1
while contador < 11:
    resultado = contador * n
    print("{} x {} = {}".format(contador, n, resultado))
    contador += 1

# 1146

while True:
    x = int(input())
    if x == 0:
        break
    for contador in range(1, x+1):
        print(contador, end=" ")

# 1134

alcool = 0
gasolina = 0
diesel = 0

while True:
    n = int(input())
    
    if n == 4:
        break
    if n == 3:
        diesel += 1
    elif n == 2:
        gasolina += 1
    elif n == 1:
        alcool += 1

print("MUITO OBRIGADO")
print("Alcool: {}".format(alcool))
print("Gasolina: {}".format(gasolina))
print("Diesel: {}".format(diesel))

# 1101

soma = 0
while True:
    comando = (str(input())).split()
    n1 = int(comando[0])
    n2 = int(comando[1])
    
    if n1 == 0 or n2 == 0:
        break
    if n1 > n2:
        for contador in range(n2, n1+1):
            print(contador, end=" ")
            soma += contador
        print("Sum = {}".format(soma))
        soma = 0
    elif n2 > n1:
        for contador in range(n1, n2+1):
            print(contador, end=" ")
            soma += contador
        print("Sum = {}".format(soma))
        soma = 0
        
# 1113

while True:
    a = str(input()).split()
    n1 = int(a[0])
    n2 = int(a[1])
    
    if n1 == n2:
        break
    
    if n1 > n2:
        print("Decrescente")
    elif n2 > n1:
        print("Crescente")

# 1099

quantidade = int(input())

for contador in range(0, quantidade):
    entrada = (str(input())).split()
    n1 = int(entrada[0])
    n2 = int(entrada[1])
    
    soma = 0
    if n1 > n2:
        for i in range(n2+1, n1):
            if i%2 != 0:
                soma += i
        print(soma)
    if n2 > n1:
        for i in range(n1+1, n2):
            if i%2 != 0:
                soma += i
        print(soma)

# 1021

a = float(input())
resto = 0

print("NOTAS:")
if a // 100 != 0:
    qnt = a // 100
    a = a - (qnt*100)
    print("{} nota(s) de R$ 100.00".format(int(qnt)))
else:
    print("0 nota(s) de R$ 100.00")
if a // 50 != 0:
    qnt = a // 50
    a = a - (qnt*50)
    print("{} nota(s) de R$ 50.00".format(int(qnt)))
else:
    print("0 nota(s) de R$ 50.00")
if a // 20 != 0:
    qnt = a // 20
    a = a - (qnt*20)
    print("{} nota(s) de R$ 20.00".format(int(qnt)))
else:
    print("0 nota(s) de R$ 20.00")
if a // 10 != 0:
    qnt = a // 10
    a = a - (qnt*10)
    print("{} nota(s) de R$ 10.00".format(int(qnt)))
else:
    print("0 nota(s) de R$ 10.00")
if a // 5 != 0:
    qnt = a // 5
    a = a - (qnt*5)
    print("{} nota(s) de R$ 5.00".format(int(qnt)))
else:
    print("0 nota(s) de R$ 5.00")
if a // 2 != 0:
    qnt = a // 2
    a = a - (qnt*2)
    print("{} nota(s) de R$ 2.00".format(int(qnt)))
else:
    print("0 nota(s) de R$ 2.00")
print("MOEDAS:")
if a // 1 != 0:
    qnt = a // 1
    a = a - (qnt*1)
    print("{} moeda(s) de R$ 1.00".format(int(qnt)))
else:
    print("0 moeda(s) de R$ 1.00")
if a // 0.5 != 0:
    qnt = a // 0.5
    a = a - (qnt*0.5)
    print("{} moeda(s) de R$ 0.50".format(int(qnt)))
else:
    print("0 moeda(s) de R$ 0.50")
if a // 0.25 != 0:
    qnt = a // 0.25
    a = a - (qnt*0.25)
    print("{} moeda(s) de R$ 0.25".format(int(qnt)))
else:
    print("0 moeda(s) de R$ 0.25")
if a // 0.10 != 0:
    qnt = a // 0.10
    a = a - (qnt*0.10)
    print("{} moeda(s) de R$ 0.10".format(int(qnt)))
else:
    print("0 moeda(s) de R$ 0.10")
if a // 0.05 != 0:
    qnt = a // 0.05
    a = a - (qnt*0.05)
    print("{} moeda(s) de R$ 0.05".format(int(qnt)))
else:
    print("0 moeda(s) de R$ 0.05")
if a // 0.01 != 0:
    qnt = a // 0.01
    a = a - (qnt*0.01)
    print("{} moeda(s) de R$ 0.01".format(int(qnt)))
else:
    print("0 moeda(s) de R$ 0.01")

# 1247

# 1708

entrada = (str(input())).split()
mais_rapido = int(entrada[0])
mais_lento = int(entrada[1])
volta = 1
while True:
    vantagem = (mais_lento * volta) - (mais_rapido * volta)
    if vantagem >= mais_lento:
        break
    volta += 1
print(volta)

# 2418

# 2247

# 2187

# 2376

# 2229