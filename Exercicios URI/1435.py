while True:
    n = int(input())
    if n == 0:
        break

    # Gerar matriz nxn com todos os termos = 0
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        matriz.append(linha)
    
    # for loop que monta a matriz
    '''
    Como funciona:
    1. Preenche todas os espaços com o primeiro número da (contagem + 1). ------A contagem é o número definido em numero_maximo e será o
    número máximo que aparecerá na matriz (no centro dela). Note que n^2 número serão preenchidos. Para uma matriz de n = 5,
    serão 25 números modificados.
    0 0 0 0 0     1 1 1 1 1
    0 0 0 0 0     1 1 1 1 1
    0 0 0 0 0  >  1 1 1 1 1
    0 0 0 0 0     1 1 1 1 1
    0 0 0 0 0     1 1 1 1 1
    
    2. Preenche (n-2)^2 vezes os números do centro com o segundo número da (contagem + 1). Para uma matriz n = 5, serão 9 números
    preenchidos
    1 1 1 1 1     1 1 1 1 1
    1 1 1 1 1     1 2 2 2 1
    1 1 1 1 1  >  1 2 2 2 1
    1 1 1 1 1     1 2 2 2 1
    1 1 1 1 1     1 1 1 1 1
    
    3. Repete o processo até completar a matriz. No caso, o processo será repetido (n//2)+1 vezes para números ímpares e n//2 para
    números pares. Para uma matriz 5x5 será repetido 3 vezes, para uma matriz 4x4 será repetido 2 vezes, etc.
    1 1 1 1 1     1 1 1 1 1
    1 2 2 2 1     1 2 2 2 1
    1 2 2 2 1  >  1 2 3 2 1
    1 2 2 2 1     1 2 2 2 1
    1 1 1 1 1     1 1 1 1 1
    
    O for de fora vai de dois em dois (n//2) vezes
    A variável repetições irá ser o tamanho da matriz menos o contador do for de fora;
    Por esse motivo que esse for irá pular de 2 em dois, essa variável contém o número que ao quadrado diz quantas vezes ocorrerá
    a substituição do número (contador//2)+1 dentro da matriz. O número será (contador//2)+1, //2 pois o contador pula de 2 em 2
    (queremos que os números dentro da matriz sejam de 1 em 1 e não de 2 em 2) e +1 pois o contador começa em 0 e queremos que os
    números comecem em 1.
    Para que a posição do número que será substituído pelo contador atual seja escolhida corretamente (sem que os números fiquem
    alinhados na esquerda da matriz, que ocorre com matriz[i][j] = (x//2)+1, mas sim fiquem centralizados), a posição é ij somados
    com a metade inteira do contador. Então se o contador for 2, os elementos serão posicionados com 1 de distância da esquerda da
    matriz (e o número colocado será 2), se o contador for 4, com 2 de distância (e o número colocado será 3).
    '''
    for x in range(0, n, 2):
        repeticoes = n-x 
        for i in range(repeticoes):
            for j in range(repeticoes):
                matriz[i+(x//2)][j+(x//2)] = (x//2)+1
    
    # Printar no formato do uri
    for i in range(n):
        linha = ''
        # Soma cada elemento separado por espaço na linha
        for j in range(n):
            linha += " %3d" %matriz[i][j]
        print(linha[1:])
    print("")
        