# 1547

repetir = int(input())
for i in range(repetir):
    entrada = str(input()).split()
    
    quantidade = int(entrada[0]) # Quantidade de alunos no grupo
    numero = int(entrada[1]) # Número que deve ser adivinhado
    
    palpites = str(input()).split() # Palpites dos alunos do grupo
    
    n = 0
    menor_distancia = None
    while True:
        if n == len(palpites):
            print(aluno_menor_distancia)
            break
        
        tentativa = int(palpites[n])
        distancia = numero - tentativa # Recebe a diferênca entre o número da tentiva e o número secreto
        
        if distancia == 0:
            print(n+1)
            break
        elif distancia < 0:
            distancia = distancia * -1
        
        if menor_distancia == None:
            menor_distancia = distancia
            aluno_menor_distancia = n+1
        elif distancia < menor_distancia:
            menor_distancia = distancia
            aluno_menor_distancia = n+1
        
        n += 1

# 1743

x = str(input()).split()
y = str(input()).split()

xinv = []
for i in x:
    if i == '0':
        xinv.append('1')
    elif i == '1':
        xinv.append('0')

if y == xinv:
    print("Y")
else:
    print("N")

# 1172

x = []
for i in range(10):
    num = int(input())
    
    if num > 0:
        x.append(num)
    elif num <= 0:
        x.append(1)
    
    print("X[{}] = {}".format(i, x[i]))

# 1173

n = int(input())
lista = []
for i in range(10):
    lista.append(n)
    print("N[{}] = {}".format(i, n))
    n *= 2

# 2399

linhas = int(input())

tabuleiro = []
for i in range(linhas):
    valor = int(input())
    tabuleiro.append(valor)

for i in range(linhas):
    resultado = 0
    
    if linhas == 1:
        if tabuleiro[i] == 1:
            resultado += 1
    else:
        if i == 0:
            if tabuleiro[i] == 1:
                resultado += 1
            if tabuleiro[i+1] == 1:
                resultado += 1
        elif i == linhas-1:
            if tabuleiro[i-1] == 1:
                resultado += 1
            if tabuleiro[i] == 1:
                resultado += 1
        else:
            if tabuleiro[i-1] == 1:
                resultado += 1
            if tabuleiro[i] == 1:
                resultado += 1
            if tabuleiro[i+1] == 1:
                resultado += 1
        
    print(resultado)