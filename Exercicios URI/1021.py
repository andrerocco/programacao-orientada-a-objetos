# 1021

valor = float(input())

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0

if valor >= 100:
    multiplo = int(valor // 100)
    n100 += multiplo
    valor -= multiplo * 100
if valor >= 50:
    multiplo = int(valor // 50)
    n50 += multiplo
    valor -= multiplo * 50
if valor >= 20:
    multiplo = int(valor // 20)
    n20 += multiplo
    valor -= multiplo * 20
if valor >= 10:
    multiplo = int(valor // 10)
    n10 += multiplo
    valor -= multiplo * 10
if valor >= 5:
    multiplo = int(valor // 5)
    n5 += multiplo
    valor -= multiplo * 5
if valor >= 2:
    multiplo = int(valor // 2)
    n2 += multiplo
    valor -= multiplo * 2

m100 = 0
m50 = 0
m25 = 0
m10 = 0
m5 = 0
m1 = 0

if valor >= 1:
    multiplo = int(valor // 1)
    m100 += multiplo
    valor -= multiplo
if valor >= 0.5:
    multiplo = int(valor // 0.5)
    m50 += multiplo
    valor -= multiplo * 0.5
if valor >= 0.25:
    multiplo = int(valor // 0.25)
    m25 += multiplo
    valor -= multiplo * 0.25
if valor >= 0.1:
    multiplo = int(valor // 0.1)
    m10 += multiplo
    valor -= multiplo * 0.1
if valor >= 0.05:
    multiplo = int(valor // 0.05)
    m5 += multiplo
    valor -= multiplo * 0.05
if valor >= 0.01:
    multiplo = int(valor // 0.01)
    m1 += multiplo
    valor -= multiplo * 0.01
    
print('NOTAS:')
notas = {100:n100,50:n50,20:n20,10:n10,5:n5,2:n2}
for nota,quantidade in notas.items():
    print("{} nota(s) de R$ {:.2f}".format(quantidade, nota))

print('MOEDAS:')
moedas = {1:m100,0.5:m50,0.25:m25,0.10:m10,0.05:m5,0.01:m1}
for nota,quantidade in moedas.items():
    print("{} nota(s) de R$ {:.2f}".format(quantidade, nota))