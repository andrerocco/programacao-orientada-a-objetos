from copy import deepcopy

# Função que retorna False se qualquer elemento da linha digitada for diferente de 0 ou 1, caso contrário retorna True
def conferir_linha(linha):
    for x in linha:
        if x != '0' and x != '1':
            return False
    return True

# Função que retorna um dicionário com as matrizes W0 até Wn
def algoritmo_de_warshall(matriz_r, n):
    # Para criar uma cópia sem vínculo entre as listas dentro da lista é usado deepcopy()
    matrizes_wi = {"W0": deepcopy(matriz_r)}
    for x in range(n):
        w_anterior = "W" + str(x)
        w_atual = "W" + str(x+1)
        matriz_temporaria = deepcopy(matrizes_wi[w_anterior])
    
        for i in range(n):
            for j in range(n):
                if matriz_temporaria[x][j] == 1 and matriz_temporaria[i][x] == 1:
                    matriz_temporaria[i][j] = 1
        matrizes_wi[w_atual] = deepcopy(matriz_temporaria)
    
    return matrizes_wi



matriz_r = []
print("Insira cada linha da matriz da relação R com os elementos separados por espaço: ")
primeira_linha = str(input()).split()

# Loop para conferir se a linha inserida está correta
while True:
    if conferir_linha(primeira_linha) == True:
        break
    else:
        print("Linha invalida, insira novamente (os valores deve ser 0's ou 1's)")
        primeira_linha = str(input()).split()

# Converter os valores para inteiros e inserir a primeira linha na matriz
primeira_linha = [int(x) for x in primeira_linha]
matriz_r.append(primeira_linha)
n = len(primeira_linha)

# Gera o input para as próximas linhas, a quantidade de vezes baseada na quantidade de elementos da primeira linha
for i in range(n-1):
    linha_seguinte = str(input()).split()
    while True:
        if conferir_linha(linha_seguinte) == True:
            break
        else:
            print("Linha invalida, insira novamente (os valores deve ser 0's ou 1's)")
            linha_seguinte = str(input()).split()
    
    linha_seguinte = [int(x) for x in linha_seguinte]
    matriz_r.append(linha_seguinte)

resultado = algoritmo_de_warshall(matriz_r, n)

# Impressão formatada do resultado
print("----- RESULTADO -----")
for w in resultado.items():
    passo = w[0]
    matriz = w[1]
    
    for linha in range(len(matriz)):
        if linha == 0:
            inicio = "{:<8}".format(passo+' =') # '^' para centralizar e '8' para dar 8 de espaço
        else:
            inicio = "{:>8}".format('')
        
        texto_linha = ''
        for elemento in matriz[linha]:
            texto_linha += "{:^3}".format(elemento)
        
        impressao = inicio + texto_linha
        print(impressao)
    
    print("\n")
