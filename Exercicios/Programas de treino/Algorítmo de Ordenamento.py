def ordenar_lista(lista):
    
    
    
    elemento_base = lista[0]
    # O elemento_base é um número escolhido como referência para ordenar a lista
    # Os números maiores que esse elemento irão para a direita e os números menores irão para a esquerda
    
    indice_inferior = 1 # Índice do elemento após o elemento base
    indice_superior = len(lista) - 1 # Índice do último elemento
    
    while True:
        print(lista)
        print("Inferior = {}".format(indice_inferior))
        print("Superior = {}".format(indice_superior))
        
        # Loop do ponteiro superior
        while indice_superior >= indice_inferior and lista[indice_superior] >= elemento_base:
            indice_superior -= 1
            # Irá descer a lista em ordem decrescente até encontrar um elemento menor que o elemento base
            # ou até atingir o ponteiro inferior
        
        # Loop do ponteiro inferior 
        while indice_inferior <= indice_superior and lista[indice_inferior] <= elemento_base:
            indice_inferior += 1
            # Processo contrário do loop relativo ao indice_superior
        
        # Nesse ponto, os dois loops já atingiram alguma das duas condições
        if indice_inferior <= indice_superior: # Se o ponteiro inferior ainda não tiver na mesma posição ou depois que o superior, então foram encontrados elementos fora de posição
            # Os elementos fora de posição encontrados trocarão de posição
            numero_menor = lista[indice_superior] # O número menor é apontado pelo índice superior pois deve ir para o lado da lista que contém os números menores que o elemento_base
            numero_maior = lista[indice_inferior] # O número maior é apontado pelo índice inferior pois deve ir para o lado da lista que contém os números maiores que o elemento_base
            # Colocando os números no lado correto
            lista[indice_inferior] = numero_menor
            lista[indice_superior] = numero_maior
        else: # Nesse ponto, a lista já está divida em números menores que elemento_base à esquerda e números maiores que elemento_base à direita
            break
    
    # Elemento diretamente abaixo da separação da lista troca de posição com o elemento base e passa a ser o primeiro da lista
    lista[0] = lista[indice_superior]
    lista[indice_superior] = elemento_base
    
    return indice_superior # Retorna o índice da da seperação da lista

    
lista = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21]
ordenar_lista(lista)