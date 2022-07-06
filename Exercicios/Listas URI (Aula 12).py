# 1164

entrada = int(input())

for j in range(entrada):
    num = int(input())

    lista_divisores = []
    for i in range(num-1, 0, -1):
        if num % i == 0:
            lista_divisores.append(i)
    
    soma_divisores = 0
    for k in lista_divisores:
        soma_divisores += k
    
    if soma_divisores == num:
        print(f"{num} eh perfeito")
    else:
        print(f"{num} nao eh perfeito")

# 1129

while True:
    casos = int(input())
    if casos == 0:
        break
    
    for n in range(casos):
        cores = [int(x) for x in str(input()).split()]
    
        assinalado = []
    
        for x in range(len(cores)):
            if cores[x] <= 127:
                assinalado.append(x)
    
        if len(assinalado) != 1:
            print("*")
        elif assinalado[0] == 0:
            print("A")
        elif assinalado[0] == 1:
            print("B")
        elif assinalado[0] == 2:
            print("C")
        elif assinalado[0] == 3:
            print("D")
        elif assinalado[0] == 4:
            print("E")

# 2392

informacoes = [int(x) for x in str(input()).split()]
pedras = informacoes[0]
sapos = informacoes[1]

info_sapos = [] # É uma lista composta por listas com [posição inicial, distância pulo]

for i in range(sapos):
    entrada = [int(x) for x in str(input()).split()]
    info_sapos.append(entrada)

lista_pedras = []
for j in range(pedras): # Gera uma lista com o número de pedras de elementos 0, como [0,0,0,0]
    lista_pedras.append(0)

# Para cada sapo da lista composta pelas informações dos sapos, preenche as possíveis posições
# que podem estar com 1 na lista_pedras. [0,0,0,0] vira por exemplo [1,1,0,1]
for sapo in info_sapos:
    sapo_pos = sapo[0]
    sapo_pulo = sapo[1]
    
    # Preenche com 1 as pedras que o sapo pode pular para trás
    i = 0
    posicao = sapo_pos
    while True:
        posicao = sapo_pos - sapo_pulo*i
        if posicao <= 0:
            break
        lista_pedras[posicao-1] = 1
        i += 1
    
    # Preenche com 1 as pedras que o sapo pode pular para frente
    i = 0
    posicao = sapo_pos
    while True:
        posicao = sapo_pos + sapo_pulo*i
        if posicao > pedras:
            break
        lista_pedras[posicao-1] = 1
        i += 1

# Imprime a lista final das pedras que podem ou não ter sapos
for x in lista_pedras:
    print(x)
