# 1261

numero_palavras, num_desc_cargos = [int(x) for x in str(input()).split()]
 
dicionario = {}
 
for i in range(numero_palavras):
    palavra, dinheiro = input().split()
    dinheiro = int(dinheiro)
    
    dicionario[palavra] = dinheiro
 
for i in range(num_desc_cargos):
    descricao = ''
    while True:
        frase = input()
        if frase == '.':
            break
        descricao += frase + ' '
    
    descricao = descricao.split()
    
    salario = 0
    
    for j in descricao:
        if j in dicionario:
            salario += dicionario[j]
    print(salario)