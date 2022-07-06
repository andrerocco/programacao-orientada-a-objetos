# 1471

while True:
    num_foram, num_voltaram = [int(x) for x in input().split()]
    
    foram = []
    contador = 0
    for i in range(num_foram):
        contador += 1
        foram.append(contador)
    
    voltaram = [int(x) for x in input().split()]
    
    if foram == sorted(voltaram):
        print("*")
        break
    
    else:
        morreram = []
        for elemento in foram:
            if elemento not in voltaram:
                morreram.append(elemento)
                
        print(' '.join(map(str, morreram)))


# 1961

def verificar(a, b, p):
    if abs(a-b) > p: # a função abs retorna o |x| do número
        return False
    else:
        return True

entrada = str(input()).split()
pulo, numero_canos = int(entrada[0]), int(entrada[1])

canos = [int(x) for x in input().split()]

for n in range(numero_canos - 1):
    resultado = verificar(canos[n], canos[n+1], pulo)
    if resultado == False:
        print("GAME OVER")
        break
if resultado == True:
    print("YOU WIN")

# 1514

def ninguem_resolveu_todos(numero_participantes, numero_problemas, resultados):
    for x in range(numero_participantes):
        total_acertos = 0
        for y in range(numero_problemas):
            total_acertos += resultados[x][y]
        if total_acertos == numero_problemas:
            return 0
    else:
        return 1

def todos_resolveram_um(numero_participantes, numero_problemas, resultados):
    for x in range(numero_problemas):
        total_acertos = 0
        for y in range(numero_participantes):
            total_acertos += resultados[y][x]
        
        if total_acertos == 0:
            return 0
    else:
        return 1

def nenhum_foi_resolvido_por_todos(numero_participantes, numero_problemas, resultados):
    for x in range(numero_problemas):
        total_acertos = 0
        for y in range(numero_participantes):
            total_acertos += resultados[y][x]
        
        if total_acertos == numero_participantes:
            return 0
    else:
        return 1

def todos_acertaram_algum(numero_participantes, resultados):
    acertou_algum = 0
    for x in range(numero_participantes):
        for y in resultados[x]:
            if y != 0:
                acertou_algum += 1
                break
    if acertou_algum == numero_participantes:
        return 1
    else:
        return 0

while True:
    entrada = str(input()).split()
    numero_participantes, numero_problemas = int(entrada[0]), int(entrada[1])
    
    if numero_participantes == 0 and numero_problemas == 0:
        break

    resultados = []
    for j in range(numero_participantes):
        questoes = [int(x) for x in str(input()).split()]
        resultados.append(questoes)
    
    c1 = ninguem_resolveu_todos(numero_participantes, numero_problemas, resultados)
    c2 = todos_resolveram_um(numero_participantes, numero_problemas, resultados)
    c3 = nenhum_foi_resolvido_por_todos(numero_participantes, numero_problemas, resultados)
    c4 = todos_acertaram_algum(numero_participantes, resultados)
    caracteristicas_atingidas = c1 + c2 + c3 + c4
    
    print(caracteristicas_atingidas)
