# André Amaral Rocco
# Solução aceita pelo URI

def mais_proximos(caixa, posicao, colunas, linha):
    # Percorre a linha da lista caixa para definir o ventilador mais proximo à direita e à esquerda
    # Se não existe ventilados à esquerda ou direita, as chaves do dicionário terão valor None (usado na função para atualizar a posição)
    pos = posicao
    proximo_esquerda = {'posicao-index': None, 'forca': None}
    proximo_direita = {'posicao-index': None, 'forca': None}
    for i in range(pos, colunas):
        if caixa[linha][i] != 0:
            proximo_direita = {'posicao-index':i, 'forca':caixa[linha][i]}
            break
    for i in range(pos, -1, -1):
        if caixa[linha][i] != 0:
            proximo_esquerda = {'posicao-index':i, 'forca':caixa[linha][i]}
            break
    return[proximo_esquerda, proximo_direita]
        
def atualizar_posicao(mais_proximo_esquerda, mais_proximo_direita, linha, posicao):
    # Usa a diferença de força entre os ventiladores encontrados para deslocar o balão
    # None ocorre para quando não há ventilador à esquerda ou direita
    if mais_proximo_esquerda['forca'] == None and mais_proximo_direita['forca'] == None:
        return posicao
    elif mais_proximo_esquerda['forca'] == None:
        deslocamento = mais_proximo_direita['forca']
        posicao['x'] -= deslocamento
        return posicao
    elif mais_proximo_direita['forca'] == None:
        deslocamento = mais_proximo_esquerda['forca']
        posicao['x'] += deslocamento
        return posicao
    # As condições None acontecem antes para que não ocorra erro no caso de comprarar uma variável None com um valor inteiro
    elif mais_proximo_esquerda['forca'] == mais_proximo_direita['forca']:
        return posicao
    elif mais_proximo_esquerda['forca'] != mais_proximo_direita['forca']:
        deslocamento = mais_proximo_esquerda['forca'] - mais_proximo_direita['forca']
        posicao['x'] += deslocamento
        return posicao
 
def conferir_status(caixa, mais_proximo_esquerda, mais_proximo_direita, linha, posicao):
    if posicao['x'] not in list(range(colunas)):
        return {'status': False, 'status_x': posicao['x'], 'status_y': posicao['y']}
    elif caixa[posicao['y']][posicao['x']] != 0:
        return {'status': False, 'status_x': posicao['x'], 'status_y': posicao['y']}
    elif posicao['y']+1 in list(range(linhas)):
        if caixa[(posicao['y']+1)][posicao['x']] != 0:
            return {'status': False, 'status_x': posicao['x'], 'status_y': posicao['y']}
        else:
            return {'status': True}
    else:
        return {'status': True}

# Remover os comentários print() e rode o código para melhor visualização do processo 

while True:
    linhas, colunas, posicao_inicial = [int(x) for x in input().split()]
    
    # Termina o programa quando o input for 0 0 0
    if linhas == 0 and colunas == 0 and posicao_inicial == 0:
        break

    # Gera a matriz composta da caixa
    caixa = []
    for i in range(linhas):
        entrada = [int(x) for x in str(input()).split()]
        caixa.append(entrada)  
    
    # Dicionário com a posição inicial x e y do balão
    posicao = {'x': (posicao_inicial-1), 'y': 0}
    
    for linha in range(len(caixa)):
        mais_proximo_esquerda, mais_proximo_direita = mais_proximos(caixa, posicao['x'], colunas, posicao['y'])
        # print(mais_proximo_esquerda)
        # print(mais_proximo_direita)

        posicao = atualizar_posicao(mais_proximo_esquerda, mais_proximo_direita, linha, posicao)
        # Atualizar o valor de 'x' na variável posição 

        resultado_temporario = conferir_status(caixa, mais_proximo_esquerda, mais_proximo_direita, linha, posicao)
        # print(resultado_temporario)
        # Se resultado_temporario['status'] retornar False o balão estorou, se retornar True não estorou

        if resultado_temporario['status'] == False:
            print('BOOM {} {}'.format(resultado_temporario['status_y']+1, resultado_temporario['status_x']+1))
            # O valor impresso é posição+1 pois a variavel posição considera o primeiro espaço como 0 (para uso mais fácil como índice da matriz caixa)
            break
        else:
            # Desce uma linha na caixa do balão
            posicao['y'] += 1
            # print(posicao)
            continue
        
    if resultado_temporario['status'] == True:
        print('OUT {}'.format(posicao['x']+1))
